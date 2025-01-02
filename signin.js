const validateEmail =  email => /^[^\s@]+@[^\s@]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})*$/.test(email); //check email validity

    // sign in variables
const emailForSignin = document.querySelector('#email-for-sign-in');
const passwordForSignin = document.querySelector('#passwordsi')
const button = document.querySelector('.btn');
// error + success designs
const container = document.querySelector('.formcontainer')
const error = document.createElement('div')
error.setAttribute('class', 'error')
const success = document.createElement('div')
success.setAttribute('class', 'success')

// sign in event listener
button.addEventListener('click', (e) => {
  e.preventDefault();
  error.textContent = ''
  if (emailForSignin.value === '' && passwordForSignin.value === '') {
    console.log('Both fields are empty');
    emailForSignin.style.borderColor = "Red";
    passwordForSignin.style.borderColor = "Red";
    error.textContent = "יש למלא את כל השדות"; // "Both fields must be filled"
    container.appendChild(error);
  }
  // Check if only password is empty
  else if (passwordForSignin.value === '' && emailForSignin.value !== '') {
    console.log('Password not done');
    passwordForSignin.style.borderColor = "Red";
    error.textContent = "יש למלא את הסיסמא"; // "Password must be filled"
    container.appendChild(error);
  }
  // Check if only email is empty
  else if (passwordForSignin.value !== '' && emailForSignin.value === '') {
    console.log('Email not done');
    emailForSignin.style.borderColor = "Red";
    error.textContent = "יש למלא כתובת מייל"; // "Email must be filled"
    container.appendChild(error);
  }
  // Check if email is invalid
  else if (!validateEmail(emailForSignin.value)) {
    emailForSignin.style.borderColor = "Red";
    error.textContent = "יש למלא כתובת מייל תקינה"; // "Please enter a valid email"
    container.appendChild(error);
  }
  else { // If no errors, proceed with normal behavior
    emailForSignin.style.borderColor = "#002f5f";
    passwordForSignin.style.borderColor = "#002f5f";
    console.log('Success - log in');
    success.textContent ='הכניסה בוצעה בהצלחה'
    container.appendChild(success)
  }

  // Set a timeout to clear the error message after 5 seconds
  setTimeout(() => {
    error.textContent = '';
  }, 5000);
})
