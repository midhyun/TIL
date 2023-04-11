### 01 웹을 구성하는 요소

#### 프로그래밍이란?
	- 컴퓨터와 소통하는 방법을 의미
	- 컴퓨터에게 전달하는 정보를 어떻게 보여주고 제어할지 결정 가능
	- 웹 개발을 하기 위한 언어로 브라우저와 소통

#### HTML, CSS, JavaScript
- HTML : 정보 또는 설계도
- CSS : 디자인 또는 스타일링
- JavaScript : 기능과 효과

#### 웹사이트 제작시 고려 사항
1. 웹 표준
	- 웹 사이트를 작성할 때 따라야 하는 공식 표준이나 기술 구격
2. 웹 접근성
	- 장애의 여부와 상관 없이 모두가 웹사이트를 이용할 수 있게 하는 방식
3. 크로스 브라우징
	- 모든 브라우저 또는 기기에서 사이트가 제대로 작동하도록 하는 기법

### 실습1

##### **지시사항**

1.  html5 문서를 선언하는 `<!DOCTYPE html>`을 입력합니다.
    
2.  문서의 시작과 끝을 나타내는 `<html></html>` 태그를 입력합니다.
    
3.  웹 사이트의 요약 정보를 담는 `<head></head>` 태그와, 눈에 보이는 정보를 담는 `<body></body>` 태그를 `<html>`태그 안에 입력합니다.
    
4.  `<head>` 태그 안에 문자 코드를 위한 `<meta charset="UTF-8">` 를 입력합니다. 그리고 `<title>...</title>` 입력하고, 태그 사이에 사이트의 제목을 넣습니다.
    
5.  `'안녕 엘리스!'` 문구를 웹 페이지에 나타내기 위해, `<body>` 태그 안에 `<h1 style="color:navy">안녕 엘리스!</h1>`를 입력합니다.


```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TEST</title>
</head>
<body>
    <h1 style="color:navy">안녕 엘리스!</h1>    
</body>
</html>
```

### 02 HTML 기본 태그

#### HTML 이란? (Hyper Text Markup Language)
- 웹사이트에서 눈에 보이는 정보나 특정 구역을 설정할 때 사용하는 언어

- 앵커 태그, 이미지 태그
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>엘리스 :: elice</title>
</head>
<body>
  <a href="https://www.naver.com" target="_blank">
    네이버
  </a>
  <img src="elice_logo.png" alt="엘리스 회사 로고">
</body>
</html>
```

### 03 구조를 잡을 때 사용하는 태그

#### HTML 태그 구성 요소
1. 목차
2. 본문
3. 부록

#### `<header>`, `<nav>` 태그
- `<header>` 태그 : 웹사이트의 머리글을 담는 공간
- `<nav>` 태그 : 메뉴 버튼을 담는 공간 (navigation)
	- `<ul>`, `<li>`, `<a>` 태그와 함께 사용

#### `<article>` 태그
- `<h>` 태그가 반드시 한개 이상 필요함. 웹표준, 검색엔진 노출 등

#### `<div>` 태그
- 공간 설정 작업을 할때 많이 사용함.

## **공간을 만들 때 사용하는 태그**

`<body>` 태그 안에 `<header> <main> <footer>` 태그를 사용해 웹 페이지의 상단, 본문, 하단 영역을 만들어봅시다!

-   **`<header>`** – 웹사이트 상단 영역
-   **`<nav>`** – 웹사이트 내 메뉴 버튼을 담는 공간

```
<header>
    <nav>
    ...
    </nav>
</header>
```

-   **`<main>`** – 웹사이트 본문 내용
-   **`<article>`** – 문서 내에서 독립적인 컨텐츠를 위한 공간

```
<main role="main">
    <article>
    ...
    </article>
</main>
```

-   **`<footer>`** – 웹사이트 하단 영역
-   **`<div>`** – 임의의 공간을 담는 공간

```
<footer>
    <div>
    ...
    </div>
</footer>
```


#### 실습4
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>엘리스 :: elice</title>
</head>
<body>
  <header>
    <h1><img src="elice_logo.png" alt=""></h1>
    <nav>
        <li><a href="#">홈</a></li>
        <li><a href="#">회사 소개</a></li>
        <li><a href="#">연락처</a></li>
    </nav>
  </header>
  <main role="main">
      <article>
          <h2>회사 소개</h2>
          <p>회사 소개와 관련된 본문 내용</p>
      </article>
  </main>
  <footer>
      <div>
          <p>서울시 서초구</p>
          <p>010-111-2222</p>
      </div>
  </footer>
</body>
</html>
```

### 04 HTML 태그의 두 가지 성격

#### Block 요소와 Inline 요소
> 두 요소를 구분짓는 특징 : 줄바꿈, 가로세로 , 상하배치

- **Block** : y축 정렬 형태로 출력 (줄바꿈 현상 나타남)
- **Inline** :x축 형태로 출력 (한 줄에 출력)

#### 실습5

##### **Block요소와 Inline요소**

Block(블럭) 요소는 줄바꿈 현상이 나타나는 반면, Inline(인라인) 요소는 줄바꿈 현상이 나타나지 않습니다.

Block 요소를 갖는 `<h>` 태그와 inline 요소를 갖는 `<a>` 태그를 입력하고, 위의 현상을 확인해봅시다!

### 05 CSS

#### CSS 구성 요소
- 선택자
- 속성
- 속성값
