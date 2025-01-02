const validateEmail =  email => /^[^\s@]+@[^\s@]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})*$/.test(email); //check email validity

  const firstName = document.querySelector('#first-name')
  const lastName = document.querySelector('#last-name')
  const emailForSignUp = document.querySelector('#email-for-sign-up')
  const passwordForSignUp = document.querySelector('#passwordsu')
  const error = document.createElement('div')
  error.setAttribute('class', 'error')
  const button = document.querySelector('.btn');
  const signupcontainer = document.querySelector('.formcontainer')
  button.addEventListener('click', (e) => { //sign up form even listener
    e.preventDefault();
    error.textContent = ''
    let hasError = false; // boolean to know if there are any more errors
    if (firstName.value === '') {
      console.log("no first name")
      error.textContent += "נא למלא שם פרטי.      ";
      hasError = true;
      firstName.style.borderColor = "Red";
    }

    // Check last name
    if (lastName.value === '') {
      console.log("no last name")
      error.textContent += "נא למלא שם משפחה.     ";
      hasError = true;
      lastName.style.borderColor = "Red";
    }

    // Check email
    if (emailForSignUp.value === '' || !validateEmail(emailForSignUp.value)) {
      console.log("no valid email")
      error.textContent += "נא למלא כתובת אימייל תקינה.     ";
      hasError = true;
      emailForSignUp.style.borderColor = "Red";
    }

    // Check password
    if (passwordForSignUp.value === '') {
      console.log("no password")
      error.textContent += "נא למלא סיסמא.       ";
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
    } else {
      // Append the error message to the container
      signupcontainer.appendChild(error);
    }
    // Set a timeout to clear the error message after 5 seconds
    setTimeout(() => {
      error.textContent = '';
    }, 5000);
  })


