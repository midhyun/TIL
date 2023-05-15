# 웹사이트 레이아웃

---

  

## 1. 박스 모델

**Point I**  
margin과 padding의 차이

```
<style>
    div {
    ...
    margin-left: 100px; 
    padding-left: 100px;
    }
</style>
```

-   `.margin-left`: border 바깥쪽에서 왼쪽에 여백을 만듦
-   `.padding-left`: border 안쪽에서 왼쪽에 여백을 만듦
-   top, right, bottom, left에 여백을 만들 수 있음
-   공간이 여백을 포함한 크기로 변경되는 점 유의

**Point II**  
top right bottom left 순서로 한 줄에 작성 가능

```
<style>
    div { margin: 100px 0 0 100px; }
</style
```

  

---

  

## 2. Block 요소와 Inline 요소

**Point I**  
Block 요소의 특징

```
<style>
    p {
        width: 200px;
        height: 200px;
        margin-top: 100px;
    }
</style>
```

-   `<p>` 태그가 대표적
-   줄바꿈 현상이 나타남
-   width/height 값 사용 가능 (공간 만들기 가능)
-   margin과 padding 값 사용 가능 (상하 배치 작업 가능)

**Point II**  
Inline 요소의 특징

-   줄바꿈 현상 없음
-   width/height 값 적용 불가
-   margin /padding /bottom 값 적용 불가

  

---

  

## 3. 마진 병합 현상

**Point I**  
**형제지간의 마진 병합**: margin-bottom과 bottom-top 중 **숫자가 큰 값**으로 적용

```
<div class="box1">Hello World</div>
<div class="box2">Hello World</div>
```

  

```
.box1 { margin-bottom: 150px; } /* 적용값 */
.box2 { bottom-top: 100px; }
```

**Point II**  
**부모 자식간의 마진 병합**: 자식 뿐만 아니라 부모에도 영향을 미침

```
<main role="main">
    <article>
    </article>
</main>
```

  

```
article {
    width: 200px;
    height: 200px;
    margin-top: 100px;
}
```

-   자식인 `<article>`뿐만 아니라 부모인 `<main>`에도 영향을 미침

  

---

  

## 4. 레이아웃에 영향을 미치는 속성

**Point I**  
**display**: Block과 Inline 요소의 성격을 바꿀 때 사용

```
p { display: inline; }
a { display: block; }
a {display: inline-block; }
```

-   `inline-block`을 사용하면 두 요소의 성격을 모두 가짐

**Point II**  
**float**: 선택된 요소를 왼쪽 끝 혹은 오른쪽 끝에 정렬시키고자 할 때 사용. 이름 그대로 선택자를 띄워 새로운 레이어층을 만드는 것

```
<div class="left"> Hello World </div>
<div class="right"> Hello World </div
```

  

```
.left { float: left; }
.next {float: left; }
```

**Point III**  
**clear**: float에 대한 속성을 제어하고자 할 때 사용

```
<header></header>
<aside class="left">Hello World</aside>
<main></main>
<aside class="right">Hello World</aside>
<footer></footer>
```

  

```
footer { clear: both; }
```

**Point IV**  
브라우저와 공간 사이의 공백 제거하기

```
<style>
    html, body {
        margin: 0;
        padding: 0;
    }
</style>
```

-   `<html>`과 `<body>` 태그는 margin과 padding 값을 가지므로 **초기화**를 해주어야 함

```
<style>
    * {
        margin: 0;
        padding: 0;
    }
</style>
```

-   혹은 `*`로 모든 html 태그 선택 가능