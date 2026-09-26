// Шапка и подвал КИДКОД для старых страниц.
(function () {
  function init() {
    var head = document.createElement('header');
    head.className = 'kk-legacy-header';
    head.innerHTML = '<a class="logo" href="index.html"><span class="logo-mark">&lt;/&gt;</span>КИДКОД</a>' +
      '<a class="back" href="index.html#advanced">← Все уроки</a>';
    document.body.insertBefore(head, document.body.firstChild);
    var foot = document.createElement('footer');
    foot.className = 'kk-legacy-footer';
    foot.innerHTML = '<span><b>КИДКОД</b> — вопросы по домашке пиши преподавателю</span>' +
      '<span><a href="https://t.me/kidkodschool" target="_blank" rel="noopener">Telegram</a>' +
      '<a href="https://vk.com/kidkodschool" target="_blank" rel="noopener">ВКонтакте</a>' +
      '<a href="https://kidkod.ru" target="_blank" rel="noopener">kidkod.ru</a></span>';
    document.body.appendChild(foot);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
