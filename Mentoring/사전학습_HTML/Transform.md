## **CSS Transition**

`transition`은 **특정 조건** 하에서 애니메이션이 동작되는 과정을 보여주고자 할 때 사용됩니다.

`property`, `duration`, `timing-function`, `delay` 속성을 사용하여, 마우스를 올렸을 때 가로폭이 길어지는 효과를 만들어 봅시다!

#### **Tip**

-   `transition`의 속성값들을 한 줄로 작성할 때, 나머지 속성값의 순서는 상관 없지만, 항상 `duration`이 먼저, `delay`가 나중에 작성되어야 합니다.
    
-   `.transition:hover`를 띄어쓰기 없이 작성해야 합니다.


## **CSS Animation**

`animation`은 특정 지점별로 애니메이션 효과를 적용할 때 사용됩니다.

`name`, `duration`, `timing-function`, `delay`, `iteration-count`, `direction` 속성을 사용하여, 가로폭이 반복적으로 길어지고 좁아지는 효과를 만들어 봅시다!

또한 `@keyframes changeWidth { }`를 사용하여 효과가 어떤 형태로 일어날지 정해봅시다!

## **지시사항**

1.  `animation-name`으로 `changeWidth`를 입력하여, 애니메이션의 이름을 설정합니다.
2.  `animation-duration`으로 `3s`를 입력합니다.
3.  `animation-timing-function`으로 `linear`을 입력합니다.
4.  `animation-delay`로 `1s`를 입력합니다.
5.  `animation-iteration-count`으로 `6`을 입력하여, 6번 반복하게 합니다.
6.  `animation-direction`으로 `alternate`을 입력하여, 앞뒤에서 번갈아 반복하게 합니다.
7.  `@keyframes changeWidth { }`를 작성하여 from과 to를 설정합니다. `from`은 `width: 300px;`, `to`는 `width: 600px;`로 설정합니다.

#### **Tip**

`.animation`과 `@keyframes`은 연동하기 위해 동일한 이름을 사용합니다.  
`animation`도 `transition`과 마찬가지로, 속성값들을 한 줄로 작성할 수 있습니다.

예를 들어 위 지시사항은 아래 한 줄로 작성할 수 있습니다.

```
.animation{
    animation: changeWidth 3s linear 1s 6 alternate;
}
```


## **CSS Transform & Animation**

`transform`과 `animation`을 결합하면 다양한 애니메이션 효과를 만들 수 있습니다.

해당 실습에서는 회전하는 애니메이션 효과를 만들어 봅시다!

## **지시사항**

1.  `.box1` 안에 `animation` 속성을 입력합니다.
2.  애니메이션 이름은 `rotation`으로 설정합니다.
3.  `duration`으로 `1500ms`을 입력합니다. 이때, 1000ms은 1s입니다.
4.  `timing-function`으로 `linear`을 입력합니다.
5.  `iteration-count`으로 `infinite`을 입력하여, 반복 효과가 무한으로 나타나도록 합니다.
6.  `direction`으로 `alternate`을 입력하여, 왕복 효과가 나타나도록 합니다.
7.  `@keyframes rotation { }`를 작성하여 from과 to를 설정합니다. `from`은 `transform: rotate(-10deg);`, `to`는 `transform: rotate(10deg);`로 설정합니다.

#### **Tip**

브라우저를 동작했을 때, 애니메이션 효과가 바로 나타날 수 있도록 하기 위해, `delay` 값을 생략할 수 있습니다!

```html
    .box1 {
        width: 300px;
        height: 300px;
        background-color: red;
  
        animation: rotation 1500ms linear infinite alternate;
    }
    
    @keyframes rotation {
        from {transform: rotate(-10deg);}
        to {transform: rotate(10deg);}
    }
```

## **메뉴 영역 애니메이션 구현하기**

쇼핑몰 상단의 메뉴 버튼 텍스트에 마우스를 올렸을 때, 텍스트 색깔이 변하는 애니메이션 효과를 구현해 봅시다!

## **지시사항**

1.  `index.css`파일을 열어서 아래 속성값을 작성해봅시다.
2.  효과가 동작되는 과정을 볼 수 있도록,  
    `#intro nav ul li a { }` 중괄호 안에 `transition`의 `property`와 `duration` 속성값을 `transition: ;` 형태로 추가입력합니다.

-   property 속성값 : `color`
-   duration 속성값 : `0.3s`

2.  `#intro nav ul li a:hover { }`를 입력하고, 중괄호 안에, 마우스를 올리면 바뀌고자 하는 텍스트 색깔을 `color: ;` 형태로 입력합니다. 색상은 `#917f7f`로 합니다.

#### **Tip**

다음은 index.html의 설계도면입니다. 설계도면을 보며 어떤 태그가 무엇을 나타내는지 확인하며 css 속성을 작성해 보세요!

```
<header id="intro">
    <nav>
        <ul>
            <li class="one"><a href="#">캐릭터 소개</a></li>
            <li class="two"><a href="#">줄거리</a></li>
            <li class="three"><a href="#">부록</a></li>
        </ul>
    </nav>
</header>
```

