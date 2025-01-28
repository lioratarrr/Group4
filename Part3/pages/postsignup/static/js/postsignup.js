const validatePhoneNumber = phone => /^05\d{8}$/.test(String(phone)) // check phone validity
const isValidHebrewAddress = (address) => /^[\u0590-\u05FF0-9\s\-\//]+$/.test(address);

const city = document.querySelector('#city')
const address = document.querySelector('#address')
const aptnum = document.querySelector('#aptnum')
const phonenum = document.querySelector('#phonenum')
const errormsg = document.createElement('div', )
errormsg.setAttribute('class', 'error')
const container = document.querySelector('.left-section')
const successmsg = document.createElement('div')
successmsg.setAttribute('id','successmsg')
const submit = document.querySelector('#register')
const form = document.querySelector('form')

submit.addEventListener('click',(e) => {
      e.preventDefault()
      errormsg.textContent=''
      let haserror = false; // boolean to know if there are any more errors
        if (city.value === '' || !isValidHebrewAddress(city.value)) { //check full name
          errormsg.textContent += ".נא למלא עיר      "
          haserror = true;
          city.style.borderColor = "Red"
          console.log("city null / doesn't meets requirements")
        }

        if (address.value === '' || !isValidHebrewAddress(address.value)) { // check phone
          errormsg.textContent += ".נא למלא כתובת תקינה     ";
          haserror = true;
          address.style.borderColor = "Red"
          console.log("address null / not valid")
        }

        if (aptnum.value === ''|| Number.isInteger(aptnum.value)) { //check info
          errormsg.textContent += ".נא למלא מספר דירה     ";
          haserror = true;
          aptnum.style.borderColor = "Red"
          console.log("apt num not valid / null")
        }

        if (phonenum.value === '' || !validatePhoneNumber(phonenum.value)) { // check phone
          errormsg.textContent += ".נא למלא מספר טלפון תקין     ";
          haserror = true;
          phonenum.style.borderColor = "Red"
          console.log("phone null / not valid")
          container.appendChild(errormsg)
        }

          // If there are no errors, proceed with form submission or further processing
      if (!haserror) { // if there's no error, print in console
        console.log('Submit success');
        form.submit()
      }

      container.appendChild(errormsg)
      // Set a timeout to clear the error message after 5 seconds
      setTimeout(() => { // timeout message
        errormsg.textContent = '';
        city.style.borderColor = "#102C57"
        address.style.borderColor = "#102C57"
        aptnum.style.borderColor = "#102C57"
        phonenum.style.borderColor = "#102C57"
        }, 5000)
        })
