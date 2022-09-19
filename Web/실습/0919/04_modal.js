const modalToggle = function() {
  document.querySelector('#modal-content').classList.toggle('active')
}

const modalBtn = document.querySelector('#modal-btn')
modalBtn.addEventListener('click', modalToggle)

const modal_cancel = document.querySelector('#modal-content')
modal_cancel.addEventListener('click', modalToggle)