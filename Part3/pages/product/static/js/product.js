const presaveProduct = (name, imageURLgold, imageURLsilver, description) => {
  localStorage.setItem('productName', name);
  localStorage.setItem('productImageGold', imageURLgold);
  localStorage.setItem('productImageSilver', imageURLsilver);
  localStorage.setItem('productDescription', description);
  window.location.href = 'product.html';
}

const productName = localStorage.getItem('productName');
const productImageGold = localStorage.getItem('productImageGold');
const productImageSilver = localStorage.getItem('productImageSilver');
const productDescription = localStorage.getItem('productDescription') || 'תיאור המוצר לא זמין';

const productImageElement = document.querySelector('.product-image img');
const presave = document.querySelector('.Presave');
const container = document.querySelector('#product-info');
const color = document.querySelector('#color');
const quantity = document.querySelector('#quantity');
const branch = document.querySelector('#branch');
const pickup = document.querySelector('.checkbox-container')
const success = document.createElement('div');
const error = document.createElement('div');
error.setAttribute('class', 'error');
success.setAttribute('class', 'success');

// Product data
if (productName) {
  document.getElementById('product-name').textContent = productName;
  document.getElementById('product-description').textContent = productDescription;

  if (productImageElement) {
    if (productImageGold) {
      productImageElement.src = productImageGold;
      productImageElement.alt = `${productName} זהב`;
    } else if (productImageSilver) {
      productImageElement.src = productImageSilver;
      productImageElement.alt = `${productName} כסף`;
    } else {
      productImageElement.src = '';
      productImageElement.alt = 'תמונה לא זמינה';
    }
  }
} else {
  document.getElementById('product-info').innerHTML = '<p>אין מוצר שנבחר.</p>';
}

const goldOption = color.querySelector('option[value="זהב"]');
const silverOption = color.querySelector('option[value="כסף"]');

// Handle silver and gold options visibility
if (!productImageSilver) {
  if (silverOption) silverOption.remove();
}

if (!productImageGold) {
  if (productImageSilver) {
    productImageElement.src = productImageSilver;
    productImageElement.alt = `${productName} כסף`;
  }
  if (goldOption) goldOption.remove();
}

// If only one option is available, set it as selected
if (productImageGold && !productImageSilver) {
  color.value = 'זהב';
} else if (!productImageGold && productImageSilver) {
  color.value = 'כסף';
} else {
  color.value = ''; // No option selected if neither is available
}

// Update image based on color selection
color.addEventListener('change', (e) => {
  e.preventDefault();
  if (color.value === 'כסף' && productImageSilver) {
    productImageElement.src = productImageSilver;
    productImageElement.alt = `${productName} כסף`;
  } else if (color.value === 'זהב' && productImageGold) {
    productImageElement.src = productImageGold;
    productImageElement.alt = `${productName} זהב`;
  }
});

// Toggle between gold and silver images when clicked
productImageElement.addEventListener('click', () => {
  if (productImageElement.src.includes(productImageGold) && productImageSilver) {
    productImageElement.src = productImageSilver;
    productImageElement.alt = `${productName} כסף`;
    color.value = 'כסף';
  } else if (productImageGold) {
    productImageElement.src = productImageGold;
    productImageElement.alt = `${productName} זהב`;
    color.value = 'זהב';
  }
});

// Handle form validation and submit
presave.addEventListener('click', (e) => {
  e.preventDefault();
  let hasError = false;
  error.textContent = ""; // Clear previous errors

  // Validation checks

  // Validate Color
  if (color.value === '' || color.value === 'בחר צבע') {
    error.textContent += "נא לבחור צבע. ";
    hasError = true;
    color.style.borderColor = "Red";
  } else {
    color.style.borderColor = ""; // Reset border color if valid
  }

  // Validate Quantity
  if (quantity.value === '' || quantity.value === 'בחר כמות') {
    error.textContent += "נא לבחור כמות. ";
    hasError = true;
    quantity.style.borderColor = "Red";
  } else {
    quantity.style.borderColor = ""; // Reset border color if valid
  }

  // Validate Branch (Ensuring a branch is selected)
  if (branch.value === '' || branch.value === 'בחר סניף') {
    error.textContent += "נא לבחור סניף. ";
    hasError = true;
    branch.style.borderColor = "Red";
  } else {
    branch.style.borderColor = ""; // Reset border color if valid
  }

  // If no errors, proceed to submit the order
  if (!hasError) {
    // Prepare order details
    const orderData = {
      productName: localStorage.getItem('productName'),
      productImageGold: localStorage.getItem('productImageGold'),
      productImageSilver: localStorage.getItem('productImageSilver'),
      productDescription: localStorage.getItem('productDescription'),
      color: color.value,
      quantity: quantity.value,
      branch: branch.value,  // Ensure branch is added here
      pickup: pickup.checked,
    }

    // Send the order data to the server
    fetch('/save_order', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(orderData)
    })
      .then(response => {
        console.log('Response Status:', response.status);  // Log response status

        // Check if user is not logged in (401 status)
        if (response.status === 401) {
          alert('עלייך להתחבר לאתר לפני ביצוע הזמנה');
          // Redirect to the sign-in page if the user is not logged in
          window.location.href = '/signin';  // Redirect to the sign-in page
          return; // Stop further processing
        }

        // Process the response if logged in
        return response.json();
      })
      .then(data => {
        if (data.status === 'success') {
          alert('ההזמנה נשמרה בהצלחה!');
        } else {
          alert('שגיאה בשמירת הזמנה: ' + data.message);
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }

  // Append the error message to the container
  container.appendChild(error);

  // Set timeout to clear the error message after 5 seconds
  setTimeout(() => {
    error.textContent = '';
  }, 5000);
});
