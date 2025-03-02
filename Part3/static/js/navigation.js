// Select elements: hamburger button, navbar, and content container
const hamburger = document.querySelector('.hamburger')
const navbar = document.querySelector('.navbar')
const content = document.querySelector('.content-container')
// Toggle menu visibility and shift content when clicking the hamburger button
hamburger.addEventListener('click', () => {
  navbar.classList.toggle('active') // Slide in/out the menu
  content.classList.toggle('shifted') // Move content
});
