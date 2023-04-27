## 변수 생성

변수는 데이터를 담는 공간을 의미합니다.

자바스크립트에서 변수를 생성하려면 `var 변수명;`을, 변수의 데이터를 콘솔에서 확인하려면 `console.log(변수명);`을 작성해야 합니다.

그리고 변수의 데이터를 웹 화면에 출력하기 위해서는 `document.write(변수명)`을 사용하실 수 있습니다.

```
var num
num = 1;

var str = "Hello World"
str = "Nice to meet you";

console.log(num);
console.log(str);

document.write(num);
document.write(str);
```

실습을 통해 여러 변수들을 생성하고 확인해 봅시다!

## 지시사항

1.  `var`를 사용하여 변수 `fruit`을 선언하고, 데이터 **apple**을 삽입합니다.
    
2.  `var`를 사용하여 변수 `box`를 선언하고, 데이터 **banana**를 삽입합니다.
    
3.  `document.write();`을 사용하여 변수 `fruit`과 `box`의 데이터를 확인합니다.
    
4.  변수 `box`의 데이터를 **tomato**로 변경합니다.
    
5.  `document.write();`을 사용하여 변수 `box`의 변경된 데이터를 확인합니다.
    

**출력 결과**  
![image](https://elice-api-cdn.azureedge.net/api-attachment/attachment/8cf17f22f5fd47498eab99c45e41964e/image.png)

### Tips

`document.writeln();`을 사용하면 출력값 사이에 공백을 넣을 수 있습니다.

```
document.writeln(변수명);
```


## 데이터 타입 - 문자열

문자열 데이터 타입은, 큰따옴표 또는 작은 따옴표로 작성된 데이터를 의미합니다.

```
var str1 = "Hello";
var str2 = "Bye";
var str3 = "100";
```

실습을 통해 문자열 데이터 타입을 갖는 변수를 생성해 봅시다!

## 지시사항

1.  `var`를 사용하여 문자열 변수 `str1`을 선언하고, 데이터 **“Hello World”** 을 삽입합니다.
    
2.  `var`를 사용하여 문자열 변수 `str2`을 선언하고, 데이터 **‘Nice to meet you’** 을 삽입합니다.
    
3.  `var`를 사용하여 문자열 변수 `str3`을 선언하고, 데이터 **“She’s a girl”** 을 삽입합니다.
    
4.  `document.write();` 또는 `document.writeln();`를 사용하여 세 변수들을 출력합니다.
    

## 데이터 타입 - 숫자

숫자 데이터 타입은 별도의 기호없이 숫자를 입력한 상태를 의미합니다.

```
var num1 = 30;
var num2 = 10.5;
```

실습을 통해 숫자 데이터 타입을 갖는 변수를 생성해 봅시다!

## 지시사항

1.  `var`를 사용하여 숫자 변수 `num1`을 생성하고, 데이터 **10**을 삽입합니다.
    
2.  `var`를 사용하여 숫자 변수 `num2`를 생성하고, 데이터 **3.14**을 삽입합니다.
    
3.  `document.write(num1 + num2)` 를 입력해 `num1`과 `num2`를 더한 값을 알아봅니다.

## 데이터 타입- 함수

함수는 **`function`** 키워드를 사용하여, 어떤 기능을 만들 때 사용되는 데이터 타입을 의미합니다.

함수는 **매개변수**, **인자**, **return**으로 구성되어 있습니다.

함수를 생성하는 방법은 다음 두 가지입니다.

```
var subtract = function(num1, num2) {
    return num1-num2;
}
```

```
function subtract(num1, num2) {
    return num1-num2;
}

console.log(subtract(20,10));
```

실습을 통해 덧셈 함수와 곱셈 함수를 생성해 봅시다!

## 지시사항

1.  `var`를 사용하여 함수를 선언합니다. 함수명은 `sum`, 매개변수는 `num1, num2`, `return`값은 `num1+num2`로 설정합니다.
    
2.  함수 `sum`의 인자로 `10, 20`을 넣고, `document.write();`를 사용하여 값을 확인합니다.
    
3.  `function`만을 사용하여 함수를 선언합니다. 함수명은 `mul`, 매개변수는 `num3, num4`, `return`값은 `num3 * num4`로 설정합니다.
    
4.  함수 `mul`의 인자로 `3, 4`를 넣고, `document.write();`를 사용하여 값을 확인합니다.

## 데이터 타입 - 배열

배열은 비슷한 성격을 갖고 있는 복수의 데이터를, 하나의 변수 안에 관리하기 위해 사용됩니다.

배열은 **index**와 **값**으로 구성되어 있습니다.

```
var vegetables = ["carrot", "cucmber", "onion"];
```

실습을 통해, 여러 과일들을 담고 있는 배열 fruit을 만들어 봅시다!

## 지시사항

1.  `var`를 사용하여 변수 `fruit`을 선언하고, 배열 데이터 타입인 **[“Apple”, “Banana”]** 데이터를 삽입합니다.
    
2.  `document.write();`를 사용하여 `fruit`의 데이터를 확인합니다.
    
3.  `document.write(fruit[0]);`를 입력하여, `fruit`의 배열에서 첫 번째 데이터가 무엇인지 확인합니다.
    
4.  `fruit` 배열의 첫 번째 데이터를 **“Tomato”** 로 변경합니다.
    
5.  `document.write();`를 사용하여 데이터가 올바르게 변경됐는지 확인합니다.

## 데이터 타입 - 객체

자신의 프로필 정보를 담고 있는 객체를 생성해 객체는 배열과 마찬가지로, 여러 개의 데이터를 담을 때 사용되는 데이터 타입입니다.

객체는 **프로퍼티**, **메서드**, **값**으로 구성되어 있습니다.

```
var student= {
  name : "Gildong",
  age : 19,
  skills : ["studying", "eating", "sleeping"],
  sum : function (num1, num2) {
      return num1 + num2;
  }
}
```

실습을 통해 Elice 학생의 정보를 담은 객체를 생성해 봅시다!

## 지시사항

1.  `var`를 사용하여 변수 `student`를 선언하고, 객체 데이터 타입을 넣기 위해 중괄호`{}`를 입력합니다.
    
2.  객체에 프로퍼티 `name: "Elice"`, `age:20`, `skills: ["Java", "HTML", "CSS", "JavaScript"]`를 추가합니다.
    
3.  객체에 메서드 `sum: function(num1,num2) { return num1 + num2; }`를 추가합니다.
    
4.  `student.name` 혹은 `student["name"]`을 입력하여 `name` 데이터에 접근합니다.
    
5.  `name`의 데이터를 **park**으로 변경하고, `document.write();`를 사용하여 올바르게 변경됐는지 확인합니다.
    
6.  `sum` 메서드에 인자 `10, 20`을 넣고, `document.write();`를 사용하여 올바르게 출력되는지 확인합니다.

## 데이터 타입 - undefined, null

**undefined**는 변수 안에 데이터를 입력하지 않은 상태를 의미합니다.

**null**은 개발자가 임의로 변수 안에 빈 데이터를 삽입한 상태를 의미합니다.

```
var unde;  //undefined
var empty = null;  //null
```

실습을 통해 undefined, null 데이터 타입을 갖는 변수를 생성해 봅시다!

## 지시사항

1.  아무 데이터도 넣지 않은 변수 `str1`을 생성하고, `document.write()`로 어떻게 출력되는지 확인합니다.
    
2.  데이터 `null`값을 넣은 변수 `empty`를 생성하고, `document.write()`로 어떻게 출력되는지 확인합니다.

## 데이터 타입 - Boolean

**Boolean**은 참 또는 거짓인 상태를 의미합니다.

```
var t = true;
var f = false;
```

실습을 통해 참과 거짓 정보를 담고 있는 변수를 생성해 봅시다!

## 지시사항

1.  `true` 값을 갖는 변수 `t`를 선언합니다.
    
2.  `false` 값을 갖는 변수 `f`를 선언합니다.
    
3.  두 변수를 `document.write()`로 출력하여 데이터를 확인합니다.


## 프로퍼티와 메서드 - 문자열

문자열 메서드로는 `length`, `charAt`, `split` 등이 있습니다.

```
var str1 = "Hi!Elice";

str1.length;  // 8
str1.charAt(1);  // i
str1.split("!");  // [Hi, Elice]
```

실습을 통해 문자열 **“Hello World”** 에 세 가지 메서드를 적용해 봅시다!

## 지시사항

1.  문자열 **“Hello World”** 를 데이터로 갖는 변수 `str1`을 선언합니다.
    
2.  `.length`를 사용하여 변수의 길이를 확인합니다.
    
3.  `.charAt`을 사용하여 0번째 데이터를 확인합니다.
    
4.  `.split`을 사용하여 공백`" "`을 기준으로 문자열을 나눕니다.
    
5.  위 변수들을 `document.write()`로 출력하여 데이터를 확인합니다.
    

#### 주의사항

-   Hello World 입력 시 대소문자 구분을 정확하게 해주어야 해요!

## 프로퍼티와 메서드 - 배열

배열 메서드로는 `length`, `push`, `unshift`, `pop`, `shift` 등이 있습니다.

```
var fruit = ["사과", "배", "포도"];

fruit.length;  //3
fruit.push("딸기");  // ["사과", "배", "포도", "딸기"]
fruit.unshift("레몬");  // ["레몬", "사과", "배", "포도", "딸기"]
fruit.pop();  // ["레몬", "사과", "배", "포도"]
fruit.shift();  // ["사과", "배", "포도"]
```

실습을 통해 배열 **fruit**에 다섯 가지 메서드를 적용해 봅시다!

## 지시사항

1.  배열 **[“Apple”, “Banana”, “Tomato”]** 를 데이터로 갖는 변수 `fruit`을 선언합니다.
    
2.  `.length`를 사용하여 변수의 길이를 확인합니다.
    
3.  `push`를 사용하여 배열 맨 끝에 데이터 **“A”** 를 추가합니다.
    
4.  `unshift`를 사용하여 배열 맨 앞에 데이터 **“B”** 를 추가합니다.
    
5.  `document.write();`를 사용하여 데이터가 올바르게 추가됐는지 확인합니다.
    
6.  `pop`을 사용하여 배열 맨 끝 데이터를 제거합니다.
    
7.  `shift`를 사용하여 배열 맨 앞 데이터를 제거합니다.
    
8.  `document.write();`를 사용하여 데이터가 올바르게 제거됐는지 확인합니다.

## 프로퍼티와 메서드 - Math

Math 객체의 메서드로는 `abs`, `ceil`, `floor`, `random` 등이 있습니다.

```
Math.abs(-12);  // 12
Math.ceil(3.4);  // 4
Math.floor(5.6);  //5
Math.random();  // 0과 1 사이의 임의의 숫자 출력
```

실습을 통해 **Math** 객체의 메서드를 적용해 봅시다!

## 지시사항

1.  `abs`를 사용하여 **-3**의 절댓값을 구하고 `document.write()`로 출력하세요.
    
2.  `ceil`를 사용하여 **0.3**의 올림 값을 구하고 `document.write()`로 출력하세요.
    
3.  `floor`를 사용하여 **10.9**의 내림 값을 구하고 `document.write()`로 출력하세요.
    
4.  `random`을 사용하여 임의의 숫자를 구하고 `document.write()`로 출력하세요.


## 프로퍼티와 메서드 - 문자를 숫자로 변환하는 메서드

문자열 데이터 타입을 숫자열 데이터 타입으로 변환시키고자 할 때는 `parseInt()`, `parseFloat()` 메서드를 사용하면 됩니다.

```
parseInt("20.6");  // 20
parseFloat("20.6");  // 20.6
```

실습을 통해 문자열 데이터 타입 **“20.14”** 를 숫자 데이터 타입으로 바꿔 봅시다!

## 지시사항

1.  변수 str1에 문자열 데이터 **“20.14”** 를 입력합니다.
    
2.  `parseInt()`를 사용하여 str1을 정수형 데이터 타입으로 변환시킵니다.
    
3.  `parseFloat()`를 사용하여 str1을 실수형 데이터 타입으로 변환시킵니다.
    
4.  위 변수를 `document.write`로 출력하여 확인해봅시다.

## 삼각형의 넓이를 구하는 함수 생성하기

삼각형의 넓이를 구하는 함수 `triangle`을 만들어 봅시다!  
삼각형의 밑변을 나타내는 변수는 `width`, 높이를 나타내는 변수는 `height`로 선언합니다.

## 지시사항

삼각형의 밑변과 높이가 주어졌을 때 삼각형의 넓이를 구하는 함수를 만들고, 밑변이 5, 높이가 7인 삼각형의 넓이를 `document.write()`로 확인해보세요.


## 배열 안의 배열 데이터에 접근하기

배열 안의 데이터에 접근할 때는 대괄호`[ ]`를 써서 인덱싱을 하였습니다.

이번 미션에서는 배열 안의 배열에 접근해 봅시다.

## 지시사항

`arrTest`배열에서 `3000`이란 값을 찾아 `document.write()`로 출력해보세요.