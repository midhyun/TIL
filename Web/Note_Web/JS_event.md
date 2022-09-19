# JS

```
EventTarget.addEventListener(type, listener)
```



```HTML
<button>버튼</button>
<p id="counter">0</p>
<script>
    let counterNumber = 0
    // btn
	const btn = document.querySelector('#btn')
    btn.addEventListener('click', functioin() {
        console.log('버튼 클릭!')
    	counterNumber += 1
    	const counter = document.querySelector('#counter')
        counter.innerText = countNumber
    })
</script>
```

```html
<h1>
    정말 중요한 내용
</h1>
<script>
    const h1 = document.querySelector('h1')
    h1.addEventListener('copy', function(event){
        // event의 기본 동작을 막고,
        event.preventDefault()
        console.log('삐빅 복사를 할 수 없습니다.')
    })
</script>
```

