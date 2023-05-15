# 움직이는 웹사이트 제작


---

  

## 1. Transform

**Point I**  
rotate, scale

```
<style>
    .transition {
        transfrom: rotate(45deg); /* 회전 */
        transform: scale(2,3); /* 확대 축소 */
    }
</style>
```

-   `.rotate(angle)`: 입력한 각도만큼 회전하며, 음수도 입력 가능
-   `.scale(x, y)`: 숫자는 비율의 의미하며 width를 x배, height를 y배 만큼 확대

**Point II**  
skew, translate

```
<style>
    .transition {
        transform: skew(10deg, 20deg); /* 각도 변경 */
        transform: translate(100px; 200px); /* 위치 변경 */
    }
</style>
```

-   `.skew(x, y)`: x축, y축을 기준으로 입력한 각도만큼 비틂
-   `.translate(x, y)`: 선택한 오브젝트의 좌표 변경

**Point III**  
prefix 접두사

```
<style>
    .transition {
        -webkit-transform: translate(100px, 200px); /* 크롬, 사파리 */
        -moz-transform: translate(100px, 200px); /* 파이어폭스 */
        -ms-transform: translate(100px, 200px ; /* 익스플로러 9.0 */
        -o-transform: translate(100px, 200px); /* 오페라 */
    }
</style>
```

-   Transform은 CSS의 최신 버전에서만 실행 가능한 키워드이지만, prefix를 추가하면 하위 버전의 브라우저에서도 실행 가능

  

---

  

## 2. Transition

**Point I**  
property, duration

```
<style>
    .transition {
        transition-property: width;
        transition-duration: 2s;
    }
</style>
```

-   `.property`: 효과를 적용하고자 하는 css 속성
-   `.duration`: 효과가 나타나는데 걸리는 시간

**Point II**  
timing-function, delay

```
<style>
    .transition {
        transition-timing-function: linear;
        transition-delay: 1s;
    }
</style>
```

-   `.timing-function`: 효과의 속도 (linear는 ‘일정하게’라는 의미)
-   `.delay`: 특정 조건 하에서 효과 발동 (1s는 ‘1초 후’라는 의미)

**Point III**  
가상 선택자: hover

```
<style>
    .transition:hover { width: 300px; }
</style>
```

-   css에서 미리 만들어 놓은 클래스로, **마우스를 올렸을 때**라는 조건
-   _Note_: `.transition:hover`를 띄어쓰기 없이 작성해야 함

종합 예시

```
<style>
    .transition {
        transition: width 2s linear 1s;
    }
    .transition:hover { width: 300px; }
</style>
```

-   마우스를 올리면 **1초 후**에 width 값이 **300px**로, **2초 동안 속도 일정**하게 변하는 애니매이션 효과 발동

  

---

  

## 3. Animation

```
.animation {
    animation-name: changeWidth; /* 애니매이션 이름 */
    animation-duration: 3s;
    animation-timing-function: linear;
    animation-delay: 1s;
    animation-iteration-count: 6;
    animation-direction: alternate;
}

@keyframes changeWidth {
    from { width: 300px; }
    to {width: 600px; ]
}
```

-   `.iteration-count`: 애니메이션 반복 횟수
-   `.direction`: 애니매이션 진행 방향
    1.  `alternate`: from → to → from
    2.  `normal`: from → to, from → to
    3.  `reverse`: to → from, to → from

  

---

  

## 4. 애니메이션 응용

**Point I**  
Transform & Animation

```
.box1 {
    animation: rotation 1500ms linear infinite alternate;
}

@keyframes rotation {
    from { transform: rotate(-10deg); }
    to { transform: rotate(10deg); }
}
```

-   애니메이션 코드를 한 줄로 작성시, 먼저 나오는 숫자가 `.duration`이고, 나중에 나오는 숫자가 `.delay`

**Point II**  
prefix 작성시 유의사항

```
.box1 {
    -webkit-animation: rotation 3s linear 1s 6 alternate;
}

@-webkit-keyframes rotation {
    from {-webkit-transform: rotate(-10deg); }
    to {-webkit-transform: rotate(10deg); }
}
```

-   prefix가 같은 애니메이션끼리 연동