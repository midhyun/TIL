# 웹사이트의 정보와 디자인

---

  

## 1. 웹을 구성하는 요소

**Point I**  
웹 구성 요소  
![](https://cdn-api.elice.io/api-attachment/attachment/15400369f2554d0c9e7c1974b16a4eaf/image.png)

**Point II**  
웹 제작시 고려 사항

1.  **웹 표준**: 웹사이트를 작성할 때 따라야 하는 공식 표준이나 기술 규격
2.  **웹 접근성**: 장애의 여부와 상관 없이 모두가 웹사이트를 이용할 수 있게 하는 방식
3.  **크로스 브라우징**: 모든 브라우저 또는 기기에서 사이트가 제대로 작동하도록 하는 기법

  

---

  

## 2. HTML 기본 태그

HTML이란 **H**yper **T**ext **M**arkup **L**anguage의 약자로, 웹사이트에서 눈에 보이는 정보나 특정 구역을 설정할 때 사용하는 언어입니다.

**Point I**  
HTML 태그 기본 구조

```
<열린태그 속성 = "속성값"> 컨텐츠 </닫힌태그>
```

-   **태그명**: HTML이 갖고 있는 고유의 기능으로, `<열린태그></닫힌태그>` 형태로 입력
-   **컨텐츠**: 열린 태그와 닫힌 태그 사이에 있는 내용물
-   **속성**: HTML 태그가 갖고 있는 추가 정보
-   **속성값**: 어떤 역할을 수행할지 구체적인 명령을 진행하는 것

**Point II**  
HTML 문서의 기본 구조  
![](https://cdn-api.elice.io/api-attachment/attachment/13ded74ec5da4244b6372241edeb78b3/image.png)

**Point III**  
HTML 기본 태그

**`<img>` 태그**: 정보성을 갖고 있는 이미지를 삽입합니다. (닫힌 태그 X)

```
<img src="logo.png" alt="회사로고">
```

-   src 속성: 삽입할 이미지 파일 경로
-   alt 속성: 웹사이트가 이미지를 출력하지 못했을 경우, 텍스트 정보로 대체

**`<h>` 태그**: heading의 약자로 제목이나 부제목을 표현합니다.

```
<h1>Hello World</h1>
<h2>Hello World</h2>
<h3>Hello World</h3>
```

-   숫자가 클수록 폰트 사이즈가 작음. 즉, 숫자는 정보의 중요도를 나타냄
-   `<h1>` 태그는 가장 중요한 정보를 담으므로, 하나의 html 문서에서 한 번만 사용됨

**`<p>` 태그**: paragraph의 약자로 본문 내용을 표현합니다.

```
<p>Nice to meet you</p>
```

-   웹사이트의 중요 정보를 담는 태그로, 나타내고자 하는 내용을 열린 태그와 닫힌 태그 사이에 입력

**`<ul>` 태그**: unordered list의 약자로, 순서가 없는 리스트 생성합니다.

```
<ul>
    <li>메뉴1</li>
    <li>메뉴2</li>
    <li>메뉴3</li>
</ul>
```

  

---

  

## 3. 구조를 잡을 때 사용하는 태그

**Point I**  
웹사이트의 **목차**를 담당하는 `<header>`, `<nav>` 태그

```
<header> <!-- 상단 영역 -->
    <nav> <!-- 메뉴 영역 -->
        ...
    </nav>
</header>
```

-   `<header>` 태그: 웹사이트의 머리글을 담는 공간
-   `<nav>` 태그: 메뉴 버튼을 담는 공간 (navigation)으로 `<ul>`, `<li>`, `<a>` 태그와 함께 사용

**Point II**  
웹사이트의 **본문**을 담당하는 `<main>`, `<article>` 태그

```
<main role="main"> <!-- 본문 영역 -->
    <article> <!-- 정보 영역 -->
        <h#></#h>
        ...
    </article>
</main>
```

-   `<main>` 태그: 문서의 주요 내용을 담는 태그 (Internet Explorer는 지원하지 않으므로 `role="main"` 속성 필수 입력)
-   `<article>` 태그: 문서의 주요 이미지나 텍스트 등의 정보를 담고 구역을 설정하는 태그로, 태그 내 구역을 대표하는 타이틀 `<#h>` 태그가 존재해야 함.

**Point III**  
웹사이트의 **부록**을 담당하는 `<footer>` 태그

```
<footer> <!-- 하단 영역 -->
    <div> <!-- 엘리스 정보 -->
        <p>주소: 대전광역시 유성구 문지로 193 KAIST</p>
        <p>이메일: contact@elice.io</p>
    </div>
    <div> <!-- 전자상거래소비자보호법 필수 정보 -->
        <p>사업자 등록번호: 000-00-00000 | 대표: 엘토끼</p>
        <p>통신판매업신고번호: 제0000-토끼굴-0000호</p>
    </div>
</footer>
```

-   `<footer>` 태그: 가장 하단에 들어가는 정보를 표기할 때 사용
-   `<div>` 태그: 임의의 공간을 만들 때 사용

  

---

  

## 4. HTML 태그의 성격

**Point I**  
Block 요소  
![](https://cdn-api.elice.io/api-attachment/attachment/8ca14b06543145509727b38518523bf9/image.png)

-   y축 정렬 형태로 출력 (줄바꿈 현상이 있음)
-   공간을 만들 수 있고, 상하 배치 작업 가능

**Point II**  
Inline 요소  
![](https://cdn-api.elice.io/api-attachment/attachment/3b22d551139b440cb2e8f3f655210517/image.png)

-   x축 정렬 형태로 출력 (한 줄에 출력)
-   공간을 만들 수 없고, 상하 배치 작업 불가능

  

---

  

## 5. CSS

CSS는 **C**ascading **S**tyle **S**heet의 약자로, HTML로 작성된 정보를 꾸며주는 언어입니다.

**Point I**  
CSS 구성 요소

```
선택자 { 속성 : 속성값; }
```

-   **선택자**: 디자인을 적용할 HTML 영역
-   **속성**: 어떤 디자인을 적용할지 정의
-   **속성값**: 어떤 역할을 수행할지 구체적으로 명령

**Point II**  
CSS 속성 (Property)

```
h1 {
    font-size: 20px; /* 폰트 사이즈 */
    font-family: sans-serif; /* 글꼴 */
    color: blue; /*폰트 색깔 */
    background-color: yellow; /* 배경색 */
    text-align: center; /* 텍스트 정렬 */
}
```

**Point III**  
CSS 연동 방법

1.  **Inline Style Sheet**: 태그 안에 직접 원하는 스타일 적용

```
<h1 style="color: red;"> coding 101 </h1>
```

  

2.  **Internal Style Sheet**: `<style>` 태그 안에 넣기

```
<head>
    <style>
        h1 { background-color: yellow;}
    </style>
</head>
```

  

3.  **External Style Sheet**: `<link>` 태그로 불러오기

```
<head>
    <link rel="stylesheet" href="style.css">
</head>
```

-   html, css 각각의 문서 안에서 따로 관리하여 상대적으로 **가독성**이 높고 **유지보수**가 쉬움

  

---

  

## 6. CSS 선택자

**Point I**  
**Type Selector**: 특정 태그에 스타일 적용

```
<!-- <h2> Type Hello World </h2> -->

<style>
    h2 { color: red; }
</style>
```

**Point II**  
**Class Selector**: 클래스 이름으로 특정 위치에 스타일 적용

```
<!-- <h2 class="coding"> Class Hello World </h2> -->
<style>
    .coding { color: blue; }
</style>
```

**Point III**  
**ID Selector**: ID를 이용해 스타일 적용

```
<!-- <h2 id="coding"> ID Hellow World </h2> -->
<style>
    #coding { color: green; }
</style>
```

  

---

  

## 7. 부모 자식 관계

![](https://cdn-api.elice.io/api-attachment/attachment/28664d8b49f34583930514f1e15cf8ec/image.png)

-   `<header>`와 `<h1>` `<p>`: 부모 자식 관계
-   `<h1>`과 `<p>`: 형제 관계
-   원하는 지역에만 css 속성을 적용하기 위해 부모를 **구체적으로** 표기

  

---

  

## 8. 캐스케이딩

**CSS의 우선순위를 결정하는 세 가지 요소**

**1. 순서**  
나중에 적용한 속성값의 우선순위가 높음

```
/* <p>Hello World</p> */

p { color: red; }
p { color: blue; ]
```

**2. 디테일**  
더 구체적으로 작성된 선택자의 우선순위가 높음

```
header p {color: red; }
p { color: blue; }
```

**3. 선택자**  
style > id > class > type 순으로 우선순위가 높음

```
<h3 style="color: pink" id="color" class="color"> color </h3>

#color { color: blue; }
.color { color: red; }
h3 {color: green; }
```

  

---

  

## 9. CSS 주요 속성

**Point I**  
width, height

```
<p class="paragraph"> 프로그래밍을 배워봐요! </p>

.paragraph { width: 500px, height: 500 px; }
```

-   `.width` 속성: 선택한 요소의 **넓이**를 설정
-   `.height` 속성: 선택한 요소의 **높이**를 설정
-   고정값은 px, 가변값은 %로 표기

**Point II**  
font

```
<p class="paragraph"> 즐거운 웹프로그래밍! </p>

.paragraph {
    font-size: 50px; /* 글자 크기 */
    font-family: Arial, sans-serif; /* 글꼴 */
    font-style: italic; /* 글자 기울기 */
    font-weight: bold; /* 글자 두께 */
```

-   `.font-family`: 브라우저마다 지원하는 폰트가 다름. 입력한 순서대로 우선순위 적용. sans-serif는 모든 브라우저에서 지원 가능하기 때문에 마지막에 작성하는 디폴트 값.
-   `.font-weight`: 100-900 사이의 숫자를 입력할 수도 있음.

**Point III**  
border

```
<p class="paragraph"> 즐거운 웹프로그래밍! </p>

.paragraph {
    width: 500px; 
    height: 500px; 
    border-style: solid;
    border-width: 10px;
    border-color: red;
    
    /* border: solid 10px red; */
```

-   `.border-style`: 실선은 solid, 점선은 dotted로 표기
-   주석과 같이 한 줄에 이어 쓸 수도 있음. 이때, 쉼표는 작성하지 않고 띄어쓰기만 함 (순서 상관 X)

**Point IV**  
background

```
<p class="paragraph"> 즐거운 웹프로그래밍! </p>

.paragraph {
    background-color: yellow;
    background-image: url(이미지 경로);
    background-repeat: no-repeat;
    background-position: left;
    
    /* background: yellow url(이미지 경로) no-repeat left; */
```

-   `.background-repeat`: x축으로 반복은 repeat-x, y축으로 반복은 repeat-y, 반복하지 않은 경우 no-repeat으로 표기
-   `.background-position`: 공간 안에서 이미지의 좌표 변경 (top, bottom, center, left, right 등)
-   주석과 같이 한 줄에 이어 쓸 수도 있음. 이때, 쉼표는 작성하지 않고 띄어쓰기만 함 (순서 상관 X)