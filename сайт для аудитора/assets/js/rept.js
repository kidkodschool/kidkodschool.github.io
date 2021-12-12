
const navButton = document.querySelector('.menu-hamburger');

navButton.addEventListener('click', navEvent);

function navEvent(event) {
    navButton.classList.toggle('open');
}