// Get references for the orders toggle
const toggleArrowOrders = document.querySelector('#toggle-arrow-orders');
const ordersWrapper = document.querySelector('.orders-wrapper');
const ordersContainer = document.querySelector('.orders-container');

// Get references for the personal details toggle
const toggleArrowPersonal = document.querySelector('#toggle-arrow-personal');
const personalDetailsWrapper = document.querySelector('.personal-details-wrapper');
const personalDetailsContainer = document.querySelector('.personal-details-container');

// Toggle visibility for orders section
toggleArrowOrders.addEventListener('click', function() {
    ordersWrapper.classList.toggle('visible');
    ordersContainer.classList.toggle('visible');
});

// Toggle visibility for personal details section
toggleArrowPersonal.addEventListener('click', function() {
    personalDetailsWrapper.classList.toggle('visible');
    personalDetailsContainer.classList.toggle('visible');
});
