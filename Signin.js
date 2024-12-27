function validateEmail(email) { //checking if the email is valid
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}
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
    const firstName = document.querySelector('#first-name');
    const lastName = document.querySelector('#last-name');
    const emailForSignUp = document.querySelector('#email-for-sign-up')
    const passwordForSignUp = document.querySelector('#passwordsu')
    const errorsignup = document.createElement('div')
    errorsignup.setAttribute('class', 'error')
    const signupcontainer = document.querySelector('#sign-up')


        // sign in event listener
        buttons[0].addEventListener('click', (e) => {
          e.preventDefault();
          if (emailForSignin.value === '' && passwordForSignin.value === '') { // if both are empty
            console.log('Both fields are empty');
            emailForSignin.style.borderColor = "Red";
            passwordForSignin.style.borderColor = "Red";
            error.textContent = "יש למלא את כל השדות"; // text
            container.appendChild(error);
          } else if (passwordForSignin.value === '' && emailForSignin.value !== '') { // only password is empty
            console.log('Password not done');
            passwordForSignin.style.borderColor = "Red";
            error.textContent = "יש למלא את הסיסמא"; // "Password must be filled"
            container.appendChild(error);
          } else if (passwordForSignin.value !== '' && emailForSignin.value === '') { // only email is empty
            console.log('Email not done');
            emailForSignin.style.borderColor = "Red";
            error.textContent = "יש למלא כתובת מייל"; // "Email must be filled"
            container.appendChild(error);
          }
          else if (!validateEmail(emailForSignin)){
              emailForSignin.style.borderColor = "Red";
            error.textContent = "יש למלא כתובת מייל תקינה"; // "Email must be filled"
            container.appendChild(error);
            }
          else { // return to normal
            emailForSignin.style.borderColor = "#002f5f"
            passwordForSignin.style.borderColor= "#002f5f"
            console.log('Entered correctly');
          }

          // Set a timeout to clear the error message after 5 seconds
          setTimeout(() => { // timeout message
            error.textContent = '';
          }, 5000)
        }
        )

        buttons[1].addEventListener('click', (e) => { //sign up form even listener
          e.preventDefault();
          let hasError = false; // boolean to know if there are any more errors
            if (firstName.value === '') { //check first name
                errorsignup.textContent += "נא למלא שם פרטי.      "
                hasError = true;
                firstName.style.borderColor = "Red"

            }

            if (lastName.value === '') { // check last name
                errorsignup.textContent += "נא למלא שם משפחה.     ";
                hasError = true;
                lastName.style.borderColor = "Red"
            }

            if (emailForSignUp.value === '') { //check email
                errorsignup.textContent += "נא למלא אימייל.     ";
                hasError = true;
                emailForSignUp.style.borderColor ="Red"
            }

            if (passwordForSignUp.value === '') { // check password
                errorsignup.textContent += "נא למלא סיסמא.       ";
                hasError = true;
                passwordForSignUp.style.borderColor = "Red"
            }

            if (!validateEmail(emailForSignUp)) { //check validity of email
                errorsignup.textContent += "נא למלא כתובת מייל תקינה       ";
                hasError = true;
                emailForSignUp.style.borderColor = "Red"
            }

            // If there are no errors, proceed with form submission or further processing
            if (!hasError) { // if there's no error, print in console
                console.log('Form submitted successfully!');
                firstName.style.borderColor = "#102C57"
                lastName.style.borderColor = "#102C57"
                emailForSignUp.style.borderColor = "#102C57"
                passwordForSignUp.style.borderColor = "#102C57"

                // You can add further processing here
            }

          signupcontainer.appendChild(errorsignup) // add message
            // Set a timeout to clear the error message after 5 seconds
            setTimeout(() => { // time out message
                errorsignup.textContent = '';
            }, 5000);
        }
        )})
