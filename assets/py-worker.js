// Web Worker: запускает Python (Pyodide) в фоне, чтобы страница не зависала,
// а бесконечный цикл можно было остановить кнопкой «Стоп».
let pyodide = null;
let pendingInput = null;

self.kkInput = (prompt) => new Promise((resolve) => {
  pendingInput = resolve;
  self.postMessage({ type: 'input', prompt });
});

async function init(base) {
  // Модульный воркер: новые версии Pyodide не поддерживают классические воркеры.
  const { loadPyodide } = await import(base + 'pyodide.mjs');
  await import('./kk-prelude.js');
  pyodide = await loadPyodide({ indexURL: base });
  const dec = new TextDecoder();
  const writer = (stream) => ({
    write(buf) {
      self.postMessage({ type: stream, text: dec.decode(buf, { stream: true }) });
      return buf.length;
    },
  });
  pyodide.setStdout(writer('out'));
  pyodide.setStderr(writer('err'));
  pyodide.runPython(self.KK_PRELUDE);
}

self.onmessage = async (e) => {
  const msg = e.data;
  try {
    if (msg.type === 'init') {
      await init(msg.base);
      self.postMessage({ type: 'ready' });
    } else if (msg.type === 'input') {
      const resolve = pendingInput;
      pendingInput = null;
      if (resolve) resolve(msg.value);
    } else if (msg.type === 'run') {
      pyodide.globals.set('_kk_code', msg.code);
      const ok = await pyodide.runPythonAsync('_kk_run(_kk_code)');
      self.postMessage({ type: 'done', id: msg.id, ok });
    } else if (msg.type === 'check') {
      pyodide.globals.set('_kk_code', msg.code);
      pyodide.globals.set('_kk_tests', JSON.stringify(msg.tests));
      const res = await pyodide.runPythonAsync('_kk_check(_kk_code, _kk_tests)');
      self.postMessage({ type: 'done', id: msg.id, results: JSON.parse(res) });
    }
  } catch (err) {
    self.postMessage({ type: 'fatal', id: msg.id, error: String(err && err.message || err) });
  }
};
