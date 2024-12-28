const presave = document.querySelector('.Presave')
const container = document.querySelector('.product-info')
const success = document.createElement('div')
success.textContent = "המוצר שוריין בהצלחה"
success.setAttribute('id', 'presavetext')
presave.addEventListener('click',(e) => {
  e.preventDefault()
  console.log (container)
  container.appendChild(success)
  console.log("Presave- success")
  setTimeout(() => { // timeout message
            success.textContent = '';
            }, 5000)
}
)
