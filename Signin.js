const validateEmail =  email => /^[^\s@]+@[^\s@]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})*$/.test(email); //check email validity

document.addEventListener('DOMContentLoaded', () => {
    // sign in variables
    const emailForSignin = document.querySelector('#email-for-sign-in');
    const passwordForSignin = document.querySelector('#passwordsi')
    const buttons = document.querySelectorAll('.btn');
    // error designs
    const error = document.createElement('div')
    error.setAttribute('class', 'error')
    const container = document.querySelector('#sign-in')

    // sign up variables
    const firstName = document.querySelector('#first-name')
    const lastName = document.querySelector('#last-name')
    const emailForSignUp = document.querySelector('#email-for-sign-up')
    const passwordForSignUp = document.querySelector('#passwordsu')
    const errorsignup = document.createElement('div')
    errorsignup.setAttribute('class', 'error')
    const signupcontainer = document.querySelector('#sign-up')

        // sign in event listener
        buttons[0].addEventListener('click', (e) => {
          e.preventDefault();
          errorsignup.textContent = ''
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
    }

    // Set a timeout to clear the error message after 5 seconds
    setTimeout(() => {
        error.textContent = '';
    }, 5000);
});

        buttons[1].addEventListener('click', (e) => { //sign up form even listener
          e.preventDefault();
          errorsignup.textContent = ''
          let hasError = false; // boolean to know if there are any more errors
          if (firstName.value === '') {
              errorsignup.textContent += "נא למלא שם פרטי.      ";
              hasError = true;
              firstName.style.borderColor = "Red";
          }

          // Check last name
          if (lastName.value === '') {
              errorsignup.textContent += "נא למלא שם משפחה.     ";
              hasError = true;
              lastName.style.borderColor = "Red";
          }

          // Check email
          if (emailForSignUp.value === ''||!validateEmail(emailForSignUp.value)) {
              errorsignup.textContent += "נא למלא כתובת אימייל תקינה.     ";
              hasError = true;
              emailForSignUp.style.borderColor = "Red";
          }

          // Check password
          if (passwordForSignUp.value === '') {
              errorsignup.textContent += "נא למלא סיסמא.       ";
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
              signupcontainer.appendChild(errorsignup);
          }
          // Set a timeout to clear the error message after 5 seconds
          setTimeout(() => {
              errorsignup.textContent = '';
          }, 5000);
        })
  }
)
