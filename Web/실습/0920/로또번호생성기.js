const btn = document.querySelector('#btn')
btn.addEventListener('click', function(){
  // ballcontainer 생성, container에 삽입
  const ballContainer = document.createElement('div')
  ballContainer.classList.add('items')
  const items = document.querySelector('#number-con')
  items.appendChild(ballContainer)
  const numbers = _.sampleSize(_.range(1, 46), 6)
  console.log(numbers)
  for (i of numbers) {
    const ball = document.createElement('div')
    ball.classList.add('item')
    ball.innerText = i
    console.log(i)
    if (i > 40){
      ball.classList.add('blue')
    } else if (i > 30){
      ball.classList.add('green')
    } else if (i > 20){
      ball.classList.add('yellow')
    } else if (i > 10){
      ball.classList.add('orange')
    } else if (i > 0){
      ball.classList.add('red')
    }
    ballContainer.appendChild(ball)}
  })

