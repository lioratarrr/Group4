const validateEmail =  email => /^[^\s@]+@[^\s@]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})*$/.test(email); //check email validity
const isValidName = name => /^[a-zA-Zא-ת]+$/.test(name.trim()) && name.trim().length > 0;
// set variables
const firstName = document.querySelector('#first-name')
const lastName = document.querySelector('#last-name')
const emailForSignUp = document.querySelector('#email-for-sign-up')
const passwordForSignUp = document.querySelector('#passwordsu')
const container = document.querySelector('.formcontainer')
const button = document.querySelector('.btn');
// set success + error designs
const error = document.createElement('div')
error.setAttribute('class', 'error')
const success = document.createElement('div')
success.setAttribute('class', 'success')


button.addEventListener('click', (e) => { //sign up form even listener
  e.preventDefault();
  error.textContent = ''
  let hasError = false; // boolean to know if there are any more errors
  if (firstName.value === ''||!isValidName(firstName.value)) {
    console.log("no first name")
    error.innerHTML += ".נא למלא שם פרטי תקין<br>";
    hasError = true;
    firstName.style.borderColor = "Red";
  }

  // Check last name
  if (lastName.value === ''||!isValidName(lastName.value)) {
    console.log("no last name")
    error.innerHTML += ".נא למלא שם משפחה תקין<br>";
    hasError = true;
    lastName.style.borderColor = "Red";
  }

  // Check email
  if (emailForSignUp.value === '' || !validateEmail(emailForSignUp.value)) {
    console.log("no valid email")
    error.innerHTML += ".נא למלא כתובת אימייל תקינה<br>";
    hasError = true;
    emailForSignUp.style.borderColor = "Red";
  }

  // Check password
  if (passwordForSignUp.value === '') {
    console.log("no password")
    error.innerHTML += ".נא למלא סיסמא<br>";
    hasError = true;
    passwordForSignUp.style.borderColor = "Red";
  }

  // If there are no errors, reset the border colors and log success
  if (!hasError) {
    console.log('Sign up completed');
    firstName.style.borderColor = "#102C57";
    lastName.style.borderColor = "#102C57";
    emailForSignUp.style.borderColor = "#102C57";
    passwordForSignUp.style.borderColor = "#102C57";
    success.textContent ='ההרשמה בוצעה בהצלחה'
    container.appendChild(success)
  }

  else {
    // Append the error message to the container
    container.appendChild(error);
    }
    // Set a timeout to clear the error message after 5 seconds
    setTimeout(() => {
      error.textContent = '';
    }, 5000)
  })
