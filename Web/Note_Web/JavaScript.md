# JavaScript

```javascript
<script>
    const a = document.creatElement('a')
	a.innerText = '실라버스'
	const body = document.querySelector('body')
    body.appendChild(a)
	a.setAttribute('href','https://syllaverse.com')
	console.log(a.getAttribute('href'))
</script>
```

### DOM 선택 - 선택 관련 메서드

```javascript
document.querySelector(selector)
- 제공한 선택자와 일치하는 element 하나 선택
- 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환 (없다면 null)
document.querySelectorAll(selector)
- 제공한 선택자와 일치하는 여러 element를 선택
- 매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
- 지정된 셀렉터에 일치하는 NodeList를 반환
getElementById(id)
getElementByTagName(name)
getElementsByClassName(names)
```

##### querySelector(), querySelectorAll()을 사용하는 이유

- id, class 그리고 tag 선택자 등을 모두 사용 가능하므로, 더 구체적이고 유연하게 선택 가능
  ex) document.querySelector('#id'), document.querySelectAll('.class')

```javascript
1. 단일 element
querySelector()
2. HTMLCollection

3. NodeList
querySelectorAll()

```

### DOM 변경 - 변경 관련 메서드 (Creation)

```javascript
document.createElement()
- 작성한 태그 명의 HTML 요소를 생성하여 반환
Element.append()
- 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 Node 객체나 DOMString을 삽입
- 여러 개의 Node 객체, DOMString을 추가 할 수 있음
- 반환 값이 없음
Node.appendChild()
- 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입(Node만 추가 가능)
- 한번에 오직 하나의 Node만 추가할 수 있음
- 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 새로운 위치로 이동
Node.innerText
- Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현 (해당 요소 내부의 raw text)(사람이 읽을 수 있는 요소만 남김)
- 즉 줄바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현
Element.innerHTML
- 요소(element) 내에 포함된 HTML 마크업을 반환
- [참고]xSS 공격에 취약하므로 사용 시 주의
```

### DOM 삭제 - 삭제 관련 메서드

```javascript
ChildNode.remove()
- Node가 속한 트리에서 해당 Node를 제거
Node.removeChild()
- DOM에서 자식 Node를 제거하고 제거된 Node를 반환
- Node는 인자로 들어가는 자식 Node의 부모 Node
Element.setAttribute(name, value)
- 지정된 요소의 값을 설정
- 속성이 이미 종재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새속성을 추가
```

### DOM 조작 -정리

- 선택한다.
- 변경(조작)한다.