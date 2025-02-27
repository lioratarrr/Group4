const hamburger = document.querySelector('.hamburger')
const navbar = document.querySelector('.navbar')
const content = document.querySelector('.content-container')

hamburger.addEventListener('click', () => {
  navbar.classList.toggle('active') // Slide in/out the menu
  content.classList.toggle('shifted') // Move content
});
