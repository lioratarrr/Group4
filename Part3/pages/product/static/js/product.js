// set up variable from the previous page to plant in the product page
const presaveProduct = (name, imageURLgold, imageURLsilver, description) => {
  localStorage.setItem('productName', name)
  localStorage.setItem('productImageGold', imageURLgold)
  localStorage.setItem('productImageSilver', imageURLsilver)
  localStorage.setItem('productDescription', description)
  window.location.href = 'product.html';
}
// set up variables from the local storage
const productName = localStorage.getItem('productName')
const productImageGold = localStorage.getItem('productImageGold')
const productImageSilver = localStorage.getItem('productImageSilver')
const productDescription = localStorage.getItem('productDescription') || 'תיאור המוצר לא זמין'

// create connection to the elements in the page + errors and success
const productImageElement = document.querySelector('.product-image img')
const presave = document.querySelector('.Presave')
const container = document.querySelector('#product-info')
const color = document.querySelector('#color')
const quantity = document.querySelector('#quantity')
const branch = document.querySelector('#branch')
const success = document.createElement('div')
const error = document.createElement('div')
error.setAttribute('class', 'error')
success.setAttribute('class', 'success')

// Dynamically update the product page
if (productName) {
  document.getElementById('product-name').textContent = productName;
  document.getElementById('product-description').textContent = productDescription;

  if (productImageElement) {
    // Default to the first available image
    if (productImageGold) {
      productImageElement.src = productImageGold;
      productImageElement.alt = `${productName} זהב`;
    } else if (productImageSilver) {
      productImageElement.src = productImageSilver;
      productImageElement.alt = `${productName} כסף`;
    } else {
      productImageElement.src = ''; // No image available
      productImageElement.alt = 'תמונה לא זמינה';
    }
  }
  } else {
  // Fallback if no product data is available
  document.getElementById('product-info').innerHTML = '<p>אין מוצר שנבחר.</p>';
}

// removing unavailable options
if (!productImageGold) {
  console.log("Removing gold option");
  color.querySelector('option[value="זהב"]').remove()
}

if (!productImageSilver) {
  console.log("Removing silver option");
  color.querySelector('option[value="כסף"]').remove();
}

// change the options so if only one is available - preselect it
if (productImageGold && !productImageSilver) {
  color.value = 'זהב';
} else if (!productImageGold && productImageSilver) {
  color.value = 'כסף';
}
// change the photo according to the choice
color.addEventListener('change', (e)=> {
  e.preventDefault()
  if (color.value ===  'כסף') {
  console.log("color change silver")
  productImageElement.src = productImageSilver
    productImageElement.alt = `${productName} כסף - `
  }
})
  // check for validity of the order
  presave.addEventListener('click',(e) => {
    e.preventDefault()
    let hasError = false; // boolean to know if there are any more errors
    //check color
    if (color.value === 'בחר צבע') {
      console.log("no color picked")
      error.textContent += "נא לבחור צבע.      "
      hasError = true;
      color.style.borderColor = "Red"
    }

    // Check quantity
    if (quantity.value === 'בחר כמות') {
      console.log("no quantity picked")
      error.textContent += "נא לבחור כמות.     "
      hasError = true
      quantity.style.borderColor = "Red"
    }

    // Check branch
    if (branch.value === 'בחר סניף' ) {
      console.log("no branch picked")
      error.textContent += "נא לבחור סניף.     "
      hasError = true
      branch.style.borderColor = "Red"
    }

    if (!hasError) {
      success.textContent = "המוצר שוריין בהצלחה"
      container.appendChild(success)
      console.log("Presave- success")
      setTimeout(() => { // timeout message
        success.textContent = ''
      }, 2000)
    }

    else {
        container.appendChild(error)
    }

    setTimeout(() => {
        error.textContent = ''
    }, 5000)
  }
  )
