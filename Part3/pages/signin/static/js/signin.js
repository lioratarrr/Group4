const validateEmail =  email => /^[^\s@]+@[^\s@]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})*$/.test(email) //check email validity
const validatePassword = (password) => password.length >= 6

// sign in variables
const emailForSignin = document.querySelector('#email-for-sign-in')
const passwordForSignin = document.querySelector('#passwordsi')
const button = document.querySelector('.btn')
// error + success designs
const container = document.querySelector('.formcontainer')
const error = document.createElement('div')
error.setAttribute('class', 'error')
const success = document.createElement('div')
success.setAttribute('class', 'success')
const form = document.querySelector('form')

// sign in event listener
button.addEventListener('click', (e) => {
  e.preventDefault()
  error.textContent = ''
  if (emailForSignin.value === '' && passwordForSignin.value === '') {
    console.log('Both fields are empty')
    emailForSignin.style.borderColor = "Red"
    passwordForSignin.style.borderColor = "Red"
    error.textContent = "יש למלא את כל השדות" // "Both fields must be filled"
    container.appendChild(error)
  }
  // Check if only password is empty
  else if (passwordForSignin.value === '' && emailForSignin.value !== '') {
    console.log('Password not done')
    passwordForSignin.style.borderColor = "Red"
    error.textContent = "יש למלא את הסיסמא" // "Password must be filled"
    container.appendChild(error)
  }
  // Check if only email is empty
  else if (passwordForSignin.value !== '' && emailForSignin.value === '') {
    console.log('Email not done')
    emailForSignin.style.borderColor = "Red"
    error.textContent = "יש למלא כתובת מייל" // "Email must be filled"
    container.appendChild(error)
  }
  // Check if email is invalid
  else if (!validateEmail(emailForSignin.value)) {
    emailForSignin.style.borderColor = "Red"
    error.textContent = "יש למלא כתובת מייל תקינה" // "Please enter a valid email"
    container.appendChild(error)
  }

  else if (!validatePassword(passwordForSignin.value)) {
    passwordForSignin.style.borderColor = "Red"
    error.textContent = "הסיסמא חייבת להיות באורך מינימלי של 6 תווים" // "Password must be at least 6 characters"
    container.appendChild(error)
  }
  else { // If no errors, proceed with normal behavior

    emailForSignin.style.borderColor = "#002f5f"
    passwordForSignin.style.borderColor = "#002f5f"
    const loginData = {
      email: emailForSignin.value,
      password: passwordForSignin.value
    };
    fetch('/signin', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(loginData)
    })
    .then(response => response.json())
    .then(data => {
      if (data.status === 'success') {
        // Show success message and redirect
        success.textContent = data.message
        container.appendChild(success)
        window.location.href = data.redirect
      } else {
        // Show error message
        error.textContent = data.message
        container.appendChild(error)
      }
    })
    .catch(error => {
      console.error('Error:', error)
      error.textContent = 'אירעה שגיאה. אנא נסה שוב מאוחר יותר'
      container.appendChild(error)
    })
  }


  // Set a timeout to clear the error message after 5 seconds
  setTimeout(() => {
    error.textContent = ''
  }, 5000)
})
