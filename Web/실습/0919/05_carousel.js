let idx = 0
const nextbtn = document.querySelector('#nextBtn')
nextbtn.addEventListener('click', function() {
  idx += 1
  const curElement = document.querySelector('.active')
  const items = document.querySelectorAll('.carousel-item')
  curElement.classList.toggle('active')
  items[idx%items.length].classList.toggle('active')
})
const prevbtn = document.querySelector('#prevBtn')
prevbtn.addEventListener('click', function() {
  idx -= 1
  if (idx == -1){
    idx = 3
  }
  const curElement = document.querySelector('.active')
  const items = document.querySelectorAll('.carousel-item')
  curElement.classList.toggle('active')
  items[idx%items.length].classList.toggle('active')
})