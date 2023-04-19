# 모바일에 대응되는 웹사이트를 만들어 보자

---

  

## 1. 미디어쿼리 소개

**미디어쿼리**란 PC 뿐만 아니라 모바일과 태블릿에도 대응되는 반응형 또는 적응형 웹사이트를 만들 때 사용되는 CSS 구문입니다.

```
.media {
    width: 500px;
    height: 500px;
    background-color: red;
}

/* 미디어쿼리 */
@media (min-width: 320px) and (max-width: 800px) {
    width: 300px;
    height: 300px;
    background-color: yellow;
}
```

-   `min-width`와 `max-width`로 브라우저 가로폭 설정
-   브라우저의 가로폭이 최소 320px, 최대 800px이 되었을 경우, 중괄호 안의 css 속성으로 대체하겠다는 의미

  

---

  

## 2. 미디어쿼리 사용시 주의사항

**Point I**  
**viewport**: **너비**와 **배율**을 설정할 때 사용하는 메타 태그의 속성

```
<meta name-"viewport" content="width=device-width, initial-scale=1.0">
```

-   다양한 디지털 기기의 화면 상에 표시되는 영역을 의미
-   미디어쿼리가 제대로 작동하지 않는 문제가 발생할 수 있으므로 `viewport`로 너비와 배율을 설정해야 모바일에서 의도한 화면을 볼 수 있음
-   `.width=device-width`: viewport의 가로폭 = 디바이스의 가로폭
-   `.initial-scale=1.0`: 비율은 항상 1.0

**Point II**  
CSS 속성 상속

```
.media {
    width: 500px;
    height: 500px;
    background-color: yellow;
}

@media (min-width: 320px) and (max-width: 800px) {
    .media {
        width: 300px;
        height: 300px;
        background-color: none;
    }
}
```

-   미디어쿼리 외부 영역에 있는 CSS 속성을 **상속**받음
-   만약 상속을 받지 않고자 하면 속성값으로 `none` 입력

  

---

  

## 3. 미디어쿼리 적용하기

미디어쿼리를 적용해 PC 버전의 레이아웃을 모바일 버전에 적합하게 변경해 봤습니다.

**Point I**  
상단 미디어쿼리 적용하기

```
@media (min-width: 320px) and (max-width: 820px) {
    .container {
        width: 640px;
    }
    
    #intro {
        height: 160px;
    }
    #intro h1 {
        width: 100%;
    }
    #intro nav {
        width: 100%;
    }
    #intro h1 a {
        text-align: center;
        padding: 22px 0 0 0;
    }
}
```

![](https://cdn-api.elice.io/api-attachment/attachment/388f920639d34f7aa367915ca1a66aea/image.png)

**Point II**  
본문 미디어쿼리 적용하기

```
@media (min-width: 320px) and (max-width: 820px) {
    ...
    
    #main article {
        width: 100%;
        height: 420px;
    }
}
```

![](https://cdn-api.elice.io/api-attachment/attachment/477390d2ee2f47b9a99188f9c4132022/image.png)

**Point III**  
하단 미디어쿼리 적용하기

```
@media (min-width: 320px) and (max-width: 820px) {
    ...
    
    #footer {
        padding: 30px 0;
    }
    
    #footer .copyright,
    #footer .address {
        width: 100%;
    }
    
    #footer .copyright p,
    #footer .addres p {
        text-align: center;
        padding: 0;
    }
    #footer .addres p {
        padding-top: 20px;
    }
}
```