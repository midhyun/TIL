const input_t = document.querySelector('#input')
input_t.addEventListener('input', function(e) {
  console.log(e)
  console.log(e.target.value)
})