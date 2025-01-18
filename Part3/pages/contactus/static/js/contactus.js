const validatePhoneNumber = phone => /^05\d{8}$/.test(String(phone)) // check phone validity

const isFullName = value => typeof value === 'string' &&
    value.trim().split(/\s+/).length > 1 &&
    /^[a-zA-Zא-ת\s]+$/.test(value.trim())
    //contact us variables
    const fullName = document.querySelector('#full-name')
    const phone = document.querySelector('#phone')
    const info = document.querySelector('#info')
    const submit = document.querySelector('#btn-submit')
    const error = document.createElement('div')
    error.setAttribute('class', 'error')
    const errormsg = document.createElement('div', )
    errormsg.setAttribute('class', 'error')
    const infocontainer = document.querySelector('#contactus')
    const successmsg = document.createElement('div')
    successmsg.setAttribute('id','successmsg')

    submit.addEventListener('click',(e) => {
      e.preventDefault()
      errormsg.textContent=''
      let haserror = false; // boolean to know if there are any more errors
        if (fullName.value === '' || !isFullName(fullName.value)) { //check full name
          errormsg.textContent += ".נא למלא שם מלא      "
          haserror = true;
          fullName.style.borderColor = "Red"
          console.log("full name null / doesn't meets requirements")
        }

        if (phone.value === '' || !validatePhoneNumber(phone.value)) { // check phone
          errormsg.textContent += ".נא למלא מספר טלפון תקין     ";
          haserror = true;
          phone.style.borderColor = "Red"
          console.log("phone null / not valid")
        }

        if (info.value === '') { //check info
          errormsg.textContent += ".נא למלא את פרטי הפניה     ";
          haserror = true;
          info.style.borderColor = "Red"
          infocontainer.appendChild(errormsg)
          console.log("no info")
        }

          // If there are no errors, proceed with form submission or further processing
      if (!haserror) { // if there's no error, print in console
        successmsg.textContent ="בקשתך נשלחה, נציג יחזור אלייך"
        infocontainer.appendChild(successmsg)
        // Set a timeout to clear the error message after 5 seconds
        setTimeout(() => { // timeout message
          successmsg.textContent = '';
          }, 5000)
        console.log('Submit success');
        fullName.style.borderColor = "#102C57"
        phone.style.borderColor = "#102C57"
        info.style.borderColor = "#102C57"
      }

      infocontainer.appendChild(errormsg)
      // Set a timeout to clear the error message after 5 seconds
      setTimeout(() => { // timeout message
        error.textContent = '';
        }, 5000)
        })
