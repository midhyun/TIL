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


### 06 CSS 선택자

#### 선택자(Selector)
- Type : html 태그
- Class : 태그 별명
- ID : 태그 이름 (Unique)

## **CSS 선택자**

CSS 선택자로는 세 가지가 있습니다. 세 선택자를 사용해 각각의 태그에 CSS 속성을 적용해봅시다!

**1. Type 선택자 – 특정 태그에 스타일을 적용합니다.**

```
<head>
    <style>
        h1 { color: blue ; }
    </style>
</head>

<body>
    <h1>Type Elice</h1>
</body>
```

**2. Class 선택자 – `.`으로 클래스 이름을 선언하고, 해당 클래스에 스타일을 적용합니다.**

```
<head>
    <style>
        .coding { color: blue; }
    </style>
</head>

<body>
    <h1 class= "coding">Class Elice</h1>
</body>
```

**3. ID 선택자 – `#`으로 ID를 선언하고, 해당 ID에 스타일을 적용합니다.**

```
<head>
    <style>
        #coding { color: blue; }
    </style>
</head>

<body>
    <h1 id= "coding">ID Elice</h1>
</body>
```


## **CSS 속성의 상속**

부모 태그 `<header> <footer>`의 CSS 속성은 자식 태그 `<h1> <p>`가 상속 받습니다.

반대로 자식 태그의 CSS 속성은 부모 태그에 영향을 미치지 않습니다.

각 태그의 속성값을 바꿔보며 CSS 속성의 상속에 대해 알아봅시다!

## 캐스케이딩
> CSS의 우선순위를 결정하는 세 가지 요소

1. 순서
	- 나중에 작성한 선택자의 우선순위가 높음
2. 디테일
	- 더 구체적으로 작성된 선택자의 우선순위가 높음
3. 선택자
	- style > id > class > type


## **CSS 캐스케이딩**

CSS의 우선 순위를 결정하는 요소는 다음 세 가지입니다.

**1. 나중에 작성한 코드가 우선 순위를 갖습니다.**

```
p { color: red; } 
p { color: blue; }
/* blue */
```

**2. 더 구체적으로 작성한 코드가 우선 순위를 갖습니다.**

```
h3 { color: red; }
header h3 { color: blue; }
/* blue */
```

**3. 스타일, 아이디, 클래스, 타입 순으로 우선 순위를 갖습니다.**

```
h3 { color: green; }
#color { color: blue; }
/* blue */
```

특정 요소에 여러 속성을 적용하였을 때, 최종 결과물에 반영되는 CSS 코드가 무엇인지 알아봅시다!

## **CSS 주요 속성 1**

-   **`width`**, **`height`** – 요소의 넓이와 높이를 설정합니다.

```
.paragraph { width: 500px; height: 500px; }
```

-   **`font-`** – 글자 크기, 글꼴, 두께 등, 글자와 관련된 속성을 설정합니다.

```
.paragraph { 
font-size: 50px;
font-family: Arial, sans-serif;
font-style: italic;
font-weight: bold;
}
```

`<body>` 안에서 `<h1>`를 사용해 **Nice to meet you**를 출력합니다.

`<style>` 태그 안에서 클래스 이름을 호출하고, `.paragraph`의 넓이, 높이, 배경색, 그리고 글자 속성을 결정합니다.

width, height, background-color, font- 속성을 이용해 .paragraph 클래스의 넓이와 높이, 배경색 그리고 글꼴을 설정해봅시다!

## **CSS 주요 속성 2**

-   **`border-`** – 테두리의 두께, 색 등을 설정합니다.
    
    ```
    .paragraph { 
        border-style: dotted;
        border-width: 1px;
        border-color: blue;
    }
    ```
    
-   **`background-`** – 배경 색상, 이미지 등을 설정합니다.
    
    ```
    .paragraph {
        background-color: blue;
        background-image: url(이미지 경로);
        background-repeat: repeat-x;
        background-position: top;
    }
    ```
    

`border-`, `background-` 속성을 사용해, 앞서 다룬 `.paragraph` 클래스의 테두리와 배경도 설정해봅시다!