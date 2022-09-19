let countNumber = 0
const btn = document.querySelector('#btn')
btn.addEventListener('click', function() {
  countNumber += 1
  const counter = document.querySelector('#counter')
  counter.innerText = countNumber
  
})
