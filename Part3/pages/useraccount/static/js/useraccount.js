
const validatePhoneNumber = phone => /^05\d{8}$/.test(String(phone)) // check phone validity
const isValidAptNum = (aptNum) => {
    const regex = /^\d+$/
    return regex.test(aptNum) // Simple validation for apartment number: must be a positive integer
}

// Get references for the orders toggle
const toggleArrowOrders = document.querySelector('#toggle-arrow-orders')
const ordersWrapper = document.querySelector('.orders-wrapper')
const ordersContainer = document.querySelector('.orders-container')

// Get references for the personal details toggle
const toggleArrowPersonal = document.querySelector('#toggle-arrow-personal')
const personalDetailsWrapper = document.querySelector('.personal-details-wrapper')
const personalDetailsContainer = document.querySelector('.personal-details-container')

// Toggle visibility for orders section
toggleArrowOrders.addEventListener('click', function() {
    ordersWrapper.classList.toggle('visible')
    ordersContainer.classList.toggle('visible')
});

// Toggle visibility for personal details section
toggleArrowPersonal.addEventListener('click', function() {
    personalDetailsWrapper.classList.toggle('visible')
    personalDetailsContainer.classList.toggle('visible')
});

const editField = (field) => {
    const textElement = document.getElementById(`user-${field}`);  // Get the span element
    const inputContainer = document.getElementById(`${field}-edit-container`);  // Get the input container

    // Hide the text and show the input field
    textElement.style.display = 'none'
    inputContainer.style.display = 'block'
}

const submitEdit = (field) => {
    const newValue = document.getElementById(`${field}-input`).value;
    const error = document.getElementById('error-message');
    const inputField = document.getElementById(`${field}-input`);
    const submitButton = document.getElementById(`${field}-submit-button`);

    error.textContent = '';  // Reset error message
    let hasError = false;

    // Reset the input's border color and style before validation
    inputField.style.borderColor = "";

    // Validate the input values for each field
    switch (field) {
        case 'phone':
            if (!validatePhoneNumber(newValue)) {
                error.innerHTML += "נא למלא מספר טלפון תקין<br>"
                hasError = true
                inputField.style.borderColor = "Red"
            }
            break
        case 'city':
            if (newValue.trim() === '') {
                error.innerHTML += "נא למלא עיר<br>"
                hasError = true
                inputField.style.borderColor = "Red"
            }
            break;
        case 'address':
            if (newValue.trim() === '') {
                error.innerHTML += "נא למלא כתובת<br>"
                hasError = true
                inputField.style.borderColor = "Red"
            }
            break;
        case 'aptnum':
            if (!isValidAptNum(newValue)) {
                error.innerHTML += "נא למלא מספר דירה תקין<br>"
                hasError = true
                inputField.style.borderColor = "Red"
            }
            break
    }

    // If there is any error, do not submit and just return
    if (hasError) {
        submitButton.disabled = false // Ensure button remains active for re-submission
        return
    }

    // Send the new value to the server to update the user data
    fetch('/update_user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            field: field,
            new_value: newValue
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Update the UI with the new value
            document.getElementById(`user-${field}`).textContent = newValue
            // Hide the input field and show the updated text
            document.getElementById(`${field}-edit-container`).style.display = 'none'
            document.getElementById(`user-${field}`).style.display = 'inline'
        } else {
            alert('Failed to update information')
        }
    })
    .catch(error => {
        console.error('Error:', error)
    }
    )
}

const deleteOrder = async (button) => {
  // Get the order ID from the button's data-id attribute
  const orderId = button.getAttribute('data-id');

  console.log("Sending Order ID:", orderId); // Debugging

  if (!orderId) {
    alert('Missing order ID.');
    return;
  }

  try {
    // Send the delete request to Flask with the order_id
    const response = await fetch('/delete_order', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ order_id: orderId }), // Send the order_id as JSON
    });

    // Parse the response JSON
    const result = await response.json();

    if (result.success) {
      alert(result.message);  // Show success message
      button.textContent = 'ההזמנה בוטלה'; // Update button text (optional)
    } else {
      alert(result.message);  // Show error message
    }
  } catch (error) {
    console.error('Error:', error);
    alert('Error occurred while deleting the order.');
  }
};
