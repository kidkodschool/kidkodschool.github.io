let img = document.querySelector('.section-subheader-wrapper__image')

img.addEventListener('click', (e) => {
    img.classList.toggle('full')
})
const navButton = document.querySelector('.menu-hamburger');

navButton.addEventListener('click', navEvent);

function navEvent(event) {
    navButton.classList.toggle('open');
}