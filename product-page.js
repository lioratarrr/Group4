const presaveProduct = (name, imageURL) => {
  localStorage.setItem('productName', name);
  localStorage.setItem('productImage', imageURL);
  window.location.href = 'product.html';
}

const productName = localStorage.getItem('productName');
const productImage = localStorage.getItem('productImage');
const productDescription = localStorage.getItem('productDescription') || 'תיאור המוצר לא זמין';

// Dynamically update the product page
if (productName && productImage) {
  document.getElementById('product-name').textContent = productName;
  document.getElementById('product-description').textContent = productDescription;

  // Select the first element with the class 'product-image' and update the src
  const productImageElement = document.querySelector('.product-image img');  // Use the correct class and target the img tag
  if (productImageElement) {
    productImageElement.src = productImage;
    productImageElement.alt = productName;
  }
} else {
  // Fallback if no product data is available
  document.getElementById('product-info').innerHTML = '<p>אין מוצר שנבחר.</p>';
}

const presave = document.querySelector('.Presave')
const container = document.querySelector('#product-info')
const color = document.querySelector('#color')
const quantity = document.querySelector('#quantity')
const branch = document.querySelector('#branch')
const success = document.createElement('div')
const error = document.createElement('div')
error.setAttribute('class', 'error')
success.setAttribute('class', 'success')

presave.addEventListener('click',(e) => {
  e.preventDefault()
  let hasError = false; // boolean to know if there are any more errors
  if (color.value === 'בחר צבע') {
    console.log("no color picked")
    error.textContent += "נא לבחור צבע.      ";
    hasError = true;
    color.style.borderColor = "Red";
  }

  // Check last name
  if (quantity.value === 'בחר כמות') {
    console.log("no quantity picked")
    error.textContent += "נא לבחור כמות.     ";
    hasError = true;
    quantity.style.borderColor = "Red";
  }

  // Check email
  if (branch.value === 'בחר סניף' ) {
    console.log("no branch picked")
    error.textContent += "נא לבחור סניף.     ";
    hasError = true;
    branch.style.borderColor = "Red";
  }

  if (!hasError) {
    success.textContent = "המוצר שוריין בהצלחה"
    container.appendChild(success)
    console.log("Presave- success")
    setTimeout(() => { // timeout message
      success.textContent = '';
    }, 2000)
  }

  else {
      container.appendChild(error)
  }

  setTimeout(() => {
      error.textContent = '';
  }, 5000)
}
)
