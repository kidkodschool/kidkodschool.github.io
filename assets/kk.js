/* КИДКОД · домашние задания по Python
 * - тема (светлая/тёмная)
 * - прогресс по заданиям (localStorage)
 * - редактор кода (CodeMirror) и запуск Python прямо в браузере (Pyodide)
 */
(function () {
  'use strict';

  const CDN = 'https://cdn.jsdelivr.net/npm/';
  const PYODIDE_BASE = window.KK_PYODIDE_BASE || CDN + 'pyodide@314.0.7/';
  const CM_BASE = window.KK_CM_BASE || CDN + 'codemirror@5.65.21/';
  const ASSETS = (document.currentScript && document.currentScript.src.replace(/[^/]*$/, '')) || 'assets/';
  const CHECK_TIMEOUT = 8000;

  /* ---------- безопасное хранилище ---------- */
  const store = {
    get(key, def) {
      try { const v = localStorage.getItem(key); return v === null ? def : JSON.parse(v); } catch (e) { return def; }
    },
    set(key, val) {
      try { localStorage.setItem(key, JSON.stringify(val)); } catch (e) { /* приватный режим */ }
    },
    del(key) {
      try { localStorage.removeItem(key); } catch (e) { /* ignore */ }
    },
  };

  /* ---------- тема ---------- */
  function applyTheme(t) {
    if (t) document.documentElement.setAttribute('data-theme', t);
    else document.documentElement.removeAttribute('data-theme');
  }
  applyTheme(store.get('kk:theme', null));

  function currentTheme() {
    const t = document.documentElement.getAttribute('data-theme');
    if (t) return t;
    return window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  /* ---------- прогресс ---------- */
  const Progress = {
    all() { return store.get('kk:done', {}); },
    has(key) { return !!this.all()[key]; },
    set(key, val) {
      const d = this.all();
      if (val) d[key] = Date.now(); else delete d[key];
      store.set('kk:done', d);
      document.dispatchEvent(new CustomEvent('kk:progress'));
    },
  };
  window.KKProgress = Progress;

  /* ---------- утилиты ---------- */
  function el(tag, attrs, children) {
    const n = document.createElement(tag);
    if (attrs) for (const k in attrs) {
      if (k === 'class') n.className = attrs[k];
      else if (k === 'text') n.textContent = attrs[k];
      else if (k.startsWith('on')) n.addEventListener(k.slice(2), attrs[k]);
      else n.setAttribute(k, attrs[k]);
    }
    (children || []).forEach((c) => n.append(c));
    return n;
  }

  function loadScript(src) {
    return new Promise((res, rej) => {
      const s = document.createElement('script');
      s.src = src; s.onload = res; s.onerror = () => rej(new Error('Не удалось загрузить ' + src));
      document.head.append(s);
    });
  }
  function loadCss(href) {
    const l = document.createElement('link');
    l.rel = 'stylesheet'; l.href = href; document.head.append(l);
  }

  /* ---------- Python-движок ---------- */
  const HAS_JSPI = typeof WebAssembly !== 'undefined' && typeof WebAssembly.Suspending === 'function' && typeof Worker !== 'undefined';

  // Режим 1 (современные браузеры): Pyodide в Web Worker, input() прямо в консоли.
  class WorkerEngine {
    constructor() { this.worker = null; this.ready = null; this.seq = 0; this.job = null; }
    start() {
      if (this.ready) return this.ready;
      this.worker = new Worker(ASSETS + 'py-worker.js', { type: 'module' });
      this.ready = new Promise((resolve, reject) => {
        this.worker.onmessage = (e) => {
          const m = e.data;
          if (m.type === 'ready') return resolve();
          if (m.type === 'fatal' && !this.job) return reject(new Error(m.error));
          this.onMessage(m);
        };
        this.worker.onerror = (e) => reject(new Error(e.message || 'Ошибка запуска Python'));
      });
      this.worker.postMessage({ type: 'init', base: PYODIDE_BASE });
      return this.ready;
    }
    onMessage(m) {
      const job = this.job;
      if (!job) return;
      if (m.type === 'out') job.io.out(m.text);
      else if (m.type === 'err') job.io.err(m.text);
      else if (m.type === 'input') job.io.input(m.prompt).then((v) => this.worker.postMessage({ type: 'input', value: v }));
      else if (m.type === 'done' || m.type === 'fatal') {
        this.job = null;
        clearTimeout(job.timer);
        if (m.type === 'fatal') job.reject(new Error(m.error));
        else job.resolve(m);
      }
    }
    async exec(msg, io, timeout) {
      await this.start();
      if (this.job) this.stop();
      await this.start();
      return new Promise((resolve, reject) => {
        const id = ++this.seq;
        this.job = { id, io, resolve, reject };
        if (timeout) {
          this.job.timer = setTimeout(() => {
            this.job = null;
            this.stop();
            resolve({ timeout: true });
          }, timeout);
        }
        this.worker.postMessage(Object.assign({ id }, msg));
      });
    }
    run(code, io) { return this.exec({ type: 'run', code }, io); }
    check(code, tests, io) { return this.exec({ type: 'check', code, tests }, io, CHECK_TIMEOUT); }
    stop() {
      if (this.worker) this.worker.terminate();
      const job = this.job;
      this.worker = null; this.ready = null; this.job = null;
      if (job) { clearTimeout(job.timer); job.resolve({ stopped: true }); }
    }
    get canStop() { return true; }
  }

  // Режим 2 (запасной, напр. Safari): Pyodide на странице, input() через окно prompt().
  class PageEngine {
    constructor() { this.py = null; this.ready = null; this.io = null; }
    start() {
      if (this.ready) return this.ready;
      this.ready = (async () => {
        await loadScript(ASSETS + 'kk-prelude.js');
        await loadScript(PYODIDE_BASE + 'pyodide.js');
        this.py = await window.loadPyodide({ indexURL: PYODIDE_BASE });
        const dec = new TextDecoder();
        const w = (kind) => ({ write: (buf) => { if (this.io) this.io[kind](dec.decode(buf, { stream: true })); return buf.length; } });
        this.py.setStdout(w('out'));
        this.py.setStderr(w('err'));
        window.kkInput = (prompt) => {
          const v = window.prompt(prompt || 'Введите данные:');
          if (this.io) this.io.out((prompt || '') + (v === null ? '' : v) + '\n');
          return v;
        };
        this.py.runPython(window.KK_PRELUDE);
      })();
      this.ready.catch(() => { this.ready = null; });
      return this.ready;
    }
    async run(code, io) {
      await this.start();
      this.io = io;
      await new Promise((r) => setTimeout(r, 30)); // дать странице отрисовать «запуск»
      this.py.globals.set('_kk_code', code);
      const ok = this.py.runPython('_kk_run(_kk_code, True)');
      this.io = null;
      return { ok };
    }
    async check(code, tests, io) {
      await this.start();
      this.io = io;
      await new Promise((r) => setTimeout(r, 30));
      this.py.globals.set('_kk_code', code);
      this.py.globals.set('_kk_tests', JSON.stringify(tests));
      const res = this.py.runPython('_kk_check(_kk_code, _kk_tests, True)');
      this.io = null;
      return { results: JSON.parse(res) };
    }
    stop() { /* нельзя прервать синхронный код */ }
    get canStop() { return false; }
  }

  let engine = null;
  function getEngine() {
    if (!engine) engine = HAS_JSPI ? new WorkerEngine() : new PageEngine();
    return engine;
  }
  let busyBox = null; // какой блок сейчас выполняет код

  /* ---------- редактор ---------- */
  let cmPromise = null;
  function loadCodeMirror() {
    if (!cmPromise) {
      loadCss(CM_BASE + 'lib/codemirror.css');
      cmPromise = loadScript(CM_BASE + 'lib/codemirror.js')
        .then(() => Promise.all([
          loadScript(CM_BASE + 'mode/python/python.js'),
          loadScript(CM_BASE + 'addon/edit/matchbrackets.js'),
          loadScript(CM_BASE + 'addon/edit/closebrackets.js'),
        ]))
        .then(() => window.CodeMirror)
        .catch(() => null);
    }
    return cmPromise;
  }

  function makeEditor(host, value, onChange, onRun) {
    // Сначала — простой textarea (работает сразу и без интернета), потом улучшаем до CodeMirror.
    const ta = el('textarea', { class: 'py-textarea', spellcheck: 'false', autocapitalize: 'off', 'aria-label': 'Редактор кода Python' });
    ta.value = value;
    host.append(ta);
    const api = {
      get: () => ta.value,
      set: (v) => { ta.value = v; },
      focus: () => ta.focus(),
    };
    ta.addEventListener('input', () => onChange(ta.value));
    ta.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) { e.preventDefault(); onRun(); }
      else if (e.key === 'Tab' && !e.shiftKey) {
        e.preventDefault();
        const s = ta.selectionStart;
        ta.setRangeText('    ', s, ta.selectionEnd, 'end');
        onChange(ta.value);
      }
    });
    const fit = () => { ta.style.height = 'auto'; ta.style.height = Math.max(120, ta.scrollHeight + 4) + 'px'; };
    ta.addEventListener('input', fit);
    requestAnimationFrame(fit);

    loadCodeMirror().then((CM) => {
      if (!CM) return;
      const cm = CM.fromTextArea(ta, {
        mode: 'python', lineNumbers: true, indentUnit: 4, tabSize: 4, matchBrackets: true,
        autoCloseBrackets: true, viewportMargin: Infinity, lineWrapping: false,
        extraKeys: {
          Tab: (c) => (c.somethingSelected() ? c.indentSelection('add') : c.replaceSelection('    ', 'end')),
          'Shift-Tab': (c) => c.indentSelection('subtract'),
          'Ctrl-Enter': () => onRun(), 'Cmd-Enter': () => onRun(),
        },
      });
      cm.on('change', () => onChange(cm.getValue()));
      api.get = () => cm.getValue();
      api.set = (v) => cm.setValue(v);
      api.focus = () => cm.focus();
      host.classList.add('has-cm');
    });
    return api;
  }

  /* ---------- консоль ---------- */
  function makeConsole(host) {
    const pre = el('pre', { class: 'py-out', 'aria-live': 'polite' });
    host.append(pre);
    let last = null;
    function write(text, cls) {
      if (!text) return;
      if (!last || last.dataset.kind !== cls) {
        last = el('span', { class: cls || '' }); last.dataset.kind = cls || '';
        pre.append(last);
      }
      last.textContent += text;
      pre.scrollTop = pre.scrollHeight;
    }
    return {
      clear() { pre.textContent = ''; last = null; },
      out: (t) => write(t, ''),
      err: (t) => write(t, 'py-err'),
      info: (t) => write(t, 'py-info'),
      input(prompt) {
        write(prompt, '');
        return new Promise((resolve) => {
          const inp = el('input', { class: 'py-in', type: 'text', autocomplete: 'off', spellcheck: 'false', 'aria-label': prompt || 'Ввод' });
          const line = el('span', { class: 'py-in-line' }, [inp]);
          pre.append(line); last = null;
          inp.focus({ preventScroll: false });
          inp.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
              e.preventDefault();
              const v = inp.value;
              line.replaceWith(el('span', { class: 'py-typed', text: v + '\n' }));
              last = null;
              resolve(v);
            }
          });
        });
      },
    };
  }

  /* ---------- блок кода ---------- */
  function setupPyBox(box) {
    const mode = box.dataset.mode || 'editor';
    const src = box.querySelector('script[type="text/x-python"]');
    const initial = src ? src.textContent.replace(/^\n/, '').replace(/\s+$/, '') + '\n' : '';
    const key = box.dataset.key;
    const tests = box.dataset.tests ? JSON.parse(box.dataset.tests) : null;
    const draftKey = key ? 'kk:code:' + key : null;
    let code = draftKey ? store.get(draftKey, initial) : initial;

    const bar = el('div', { class: 'py-bar' });
    const title = el('span', { class: 'py-title', text: mode === 'demo' ? 'Пример работы программы' : 'Твой код' });
    const status = el('span', { class: 'py-status' });
    const btns = el('div', { class: 'py-btns' });
    bar.append(title, status, btns);

    const runBtn = el('button', { class: 'btn btn-run', type: 'button' });
    runBtn.innerHTML = mode === 'demo' ? '<span aria-hidden="true">▶</span> Запустить пример' : '<span aria-hidden="true">▶</span> Запустить';
    const stopBtn = el('button', { class: 'btn btn-ghost btn-stop', type: 'button', hidden: '' });
    stopBtn.innerHTML = '<span aria-hidden="true">■</span> Стоп';
    btns.append(runBtn);
    let checkBtn = null;
    if (tests && mode !== 'demo') {
      checkBtn = el('button', { class: 'btn btn-check', type: 'button' });
      checkBtn.innerHTML = '<span aria-hidden="true">✓</span> Проверить';
      btns.append(checkBtn);
    }
    btns.append(stopBtn);
    let resetBtn = null;
    if (mode !== 'demo') {
      resetBtn = el('button', { class: 'btn btn-ghost btn-icon', type: 'button', title: 'Вернуть исходный код', 'aria-label': 'Вернуть исходный код' });
      resetBtn.textContent = '↺';
      btns.append(resetBtn);
    }

    box.textContent = '';
    box.append(bar);

    let editor = null;
    if (mode !== 'demo') {
      const edHost = el('div', { class: 'py-editor' });
      box.append(edHost);
      editor = makeEditor(edHost, code, (v) => {
        code = v;
        if (draftKey) { if (v === initial) store.del(draftKey); else store.set(draftKey, v); }
      }, () => run());
      const hint = el('div', { class: 'py-hint', text: 'Ctrl + Enter — запустить' });
      box.append(hint);
    }
    const conHost = el('div', { class: 'py-console', hidden: '' });
    box.append(conHost);
    const con = makeConsole(conHost);
    const testsHost = el('div', { class: 'py-tests', hidden: '' });
    box.append(testsHost);

    function busy(on, text) {
      runBtn.disabled = on; if (checkBtn) checkBtn.disabled = on;
      stopBtn.hidden = !(on && getEngine().canStop);
      status.textContent = text || '';
      box.classList.toggle('is-busy', on);
    }

    async function prepare() {
      if (busyBox && busyBox !== box) busyBox.dispatchEvent(new Event('kk:stop'));
      busyBox = box;
      const eng = getEngine();
      if (!eng.ready) status.textContent = 'Загружаю Python…';
      try {
        await eng.start();
      } catch (e) {
        con.err('Не получилось загрузить Python. Проверь интернет и обнови страницу.\n' + e.message + '\n');
        conHost.hidden = false;
        throw e;
      }
      return eng;
    }

    async function run() {
      const current = editor ? editor.get() : initial;
      conHost.hidden = false; testsHost.hidden = true;
      con.clear();
      busy(true, 'Загружаю Python…');
      let eng;
      try { eng = await prepare(); } catch (e) { busy(false); return; }
      busy(true, 'Выполняется…');
      try {
        const r = await eng.run(current, con);
        if (r.stopped) con.info('\n⏹ Остановлено\n');
        else if (r.ok) con.info('\n✔ Программа завершилась\n');
      } catch (e) {
        con.err('\n' + e.message + '\n');
      }
      if (busyBox === box) busyBox = null;
      busy(false);
    }

    async function check() {
      const current = editor.get();
      testsHost.hidden = false; conHost.hidden = true;
      testsHost.textContent = '';
      busy(true, 'Загружаю Python…');
      let eng;
      try { eng = await prepare(); } catch (e) { busy(false); return; }
      busy(true, 'Проверяю…');
      let r;
      try { r = await eng.check(current, tests, con); } catch (e) { r = { error: e.message }; }
      if (busyBox === box) busyBox = null;
      busy(false);
      showResults(r);
    }

    function showResults(r) {
      testsHost.textContent = '';
      if (r.stopped) return;
      let results = r.results;
      if (r.timeout) results = [{ ok: false, label: 'Время выполнения', msg: 'Программа работает слишком долго — возможно, бесконечный цикл или лишний input().' }];
      if (r.error) results = [{ ok: false, label: 'Запуск', msg: r.error }];
      const passed = results.filter((x) => x.ok).length;
      const all = passed === results.length;
      const head = el('div', { class: 'py-tests-head ' + (all ? 'ok' : 'fail') });
      head.innerHTML = all
        ? '<span class="big">🎉</span> Все проверки пройдены! Задание решено.'
        : `<span class="big">🧐</span> Пройдено ${passed} из ${results.length}. Почти! Исправь и проверь снова.`;
      testsHost.append(head);
      const ul = el('ul', { class: 'py-tests-list' });
      results.forEach((t) => {
        const li = el('li', { class: t.ok ? 'ok' : 'fail' });
        li.append(el('span', { class: 'mark', text: t.ok ? '✓' : '✗' }), el('code', { text: t.label }));
        if (!t.ok && t.msg) li.append(el('pre', { class: 'why', text: t.msg }));
        ul.append(li);
      });
      testsHost.append(ul);
      if (all && key) {
        Progress.set(key, true);
        const task = box.closest('.task');
        if (task) { task.classList.add('just-solved'); setTimeout(() => task.classList.remove('just-solved'), 1600); }
      }
    }

    runBtn.addEventListener('click', run);
    if (checkBtn) checkBtn.addEventListener('click', check);
    stopBtn.addEventListener('click', () => getEngine().stop());
    box.addEventListener('kk:stop', () => getEngine().stop());
    if (resetBtn) resetBtn.addEventListener('click', () => {
      if (editor.get() !== initial && !confirm('Вернуть исходный код? Твои изменения удалятся.')) return;
      editor.set(initial); code = initial; if (draftKey) store.del(draftKey);
    });
  }

  /* ---------- задания: отметки «готово» ---------- */
  function setupTasks() {
    const tasks = Array.from(document.querySelectorAll('.task[data-task]'));
    tasks.forEach((t) => {
      const key = t.dataset.task;
      const btn = t.querySelector('.done-btn');
      if (btn) btn.addEventListener('click', () => Progress.set(key, !Progress.has(key)));
    });
    function refresh() {
      let done = 0;
      tasks.forEach((t) => {
        const d = Progress.has(t.dataset.task);
        if (d) done++;
        t.classList.toggle('is-done', d);
        const btn = t.querySelector('.done-btn');
        if (btn) {
          btn.setAttribute('aria-pressed', d ? 'true' : 'false');
          btn.querySelector('.lbl').textContent = d ? 'Выполнено' : 'Отметить выполненным';
        }
        const nav = document.querySelector(`.toc a[href="#${t.id}"]`);
        if (nav) nav.classList.toggle('is-done', d);
      });
      document.querySelectorAll('[data-lesson-progress]').forEach((p) => {
        const total = tasks.length;
        p.querySelector('.bar i').style.width = total ? (done / total * 100) + '%' : '0';
        p.querySelector('.cnt').textContent = `${done} из ${total}`;
      });
    }
    document.addEventListener('kk:progress', refresh);
    refresh();
  }

  /* ---------- главная: прогресс по урокам ---------- */
  function setupIndex() {
    const cards = document.querySelectorAll('.lesson-card[data-lesson]');
    if (!cards.length || !window.KK_COURSE) return;
    const map = {};
    window.KK_COURSE.forEach((l) => { map[l.id] = l; });
    function refresh() {
      const done = Progress.all();
      let total = 0, solved = 0;
      cards.forEach((c) => {
        const l = map[c.dataset.lesson];
        if (!l || !l.tasks.length) return;
        const n = l.tasks.filter((k) => done[k]).length;
        total += l.tasks.length; solved += n;
        const bar = c.querySelector('.bar i');
        if (bar) bar.style.width = (n / l.tasks.length * 100) + '%';
        const cnt = c.querySelector('.cnt');
        if (cnt) cnt.textContent = `${n}/${l.tasks.length}`;
        c.classList.toggle('is-complete', n === l.tasks.length);
      });
      const all = document.querySelector('[data-total-progress]');
      if (all) {
        all.querySelector('.bar i').style.width = total ? (solved / total * 100) + '%' : '0';
        all.querySelector('.cnt').textContent = `${solved} из ${total}`;
      }
    }
    document.addEventListener('kk:progress', refresh);
    refresh();

    const filter = document.querySelector('.lesson-search');
    if (filter) filter.addEventListener('input', () => {
      const q = filter.value.trim().toLowerCase();
      cards.forEach((c) => { c.hidden = q && !c.textContent.toLowerCase().includes(q); });
    });
  }

  /* ---------- картинки: увеличение по клику ---------- */
  function setupZoom() {
    const dlg = el('dialog', { class: 'zoom' });
    const img = el('img', { alt: '' });
    dlg.append(img);
    dlg.addEventListener('click', () => dlg.close());
    document.body.append(dlg);
    document.addEventListener('click', (e) => {
      const t = e.target.closest('img.zoomable');
      if (!t || typeof dlg.showModal !== 'function') return;
      img.src = t.currentSrc || t.src; img.alt = t.alt;
      dlg.showModal();
    });
  }

  /* ---------- шапка ---------- */
  function setupHeader() {
    const btn = document.querySelector('.theme-btn');
    if (btn) btn.addEventListener('click', () => {
      const next = currentTheme() === 'dark' ? 'light' : 'dark';
      applyTheme(next); store.set('kk:theme', next);
    });
    const reset = document.querySelector('.reset-progress');
    if (reset) reset.addEventListener('click', () => {
      if (confirm('Сбросить отметки о выполненных заданиях?')) { store.set('kk:done', {}); document.dispatchEvent(new CustomEvent('kk:progress')); }
    });
    // Подсветка текущего задания в оглавлении
    const links = document.querySelectorAll('.toc a[href^="#"]');
    if (links.length && 'IntersectionObserver' in window) {
      const io = new IntersectionObserver((entries) => {
        entries.forEach((en) => {
          if (en.isIntersecting) {
            links.forEach((a) => a.classList.toggle('is-active', a.getAttribute('href') === '#' + en.target.id));
          }
        });
      }, { rootMargin: '-30% 0px -60% 0px' });
      links.forEach((a) => { const t = document.getElementById(a.getAttribute('href').slice(1)); if (t) io.observe(t); });
    }
  }

  function init() {
    setupHeader();
    setupTasks();
    setupIndex();
    setupZoom();
    const boxes = document.querySelectorAll('.py');
    boxes.forEach(setupPyBox);
    if (document.querySelector('.py[data-mode="editor"]')) loadCodeMirror();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
