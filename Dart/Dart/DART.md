### 1.0 Hello World
-  세미콜론에 주의해야함, dart는 일부러 세미콜론을 넣지 않는 경우가 있기 때문에 javascript 나 typescript 처럼 formatter가 세미콜론을 입력해 주지않음.

### 1.1 Ther Var keyword
```dart
void main() {
	var name = 'name'; // 함수나 메서드 지역변수
	String name = 'name'; // class나 property 선언시
	name = 1; // X
	name = '1'; // O
}
```

- 변수의 값을 변경할때는 최초에 선언한 자료형과 일치해야 함.
- 명시적으로 변수의 타입을 선언할 수 있고 var로 변수를 선언 할 수 있음.
	- 관습적으로 함수나 메서드 내부에 지역 변수를 선언할 때에는 var를 사용
	- class나 property를 선언할 때에는 타입을 지정함 `String`
- 변수는 데이터 타입만 일치한다면 업데이트가 가능함.

### 1.2 Dynamic Type
- 여러가지 타입을 가질 수 있는 변수에 사용되는 키워드
- 사용하는게 추천되진 않지만 때떄로 유용함.
- dynamic은 정말로 필요할 때만 사용할 것

```dart
void main() {
	var name;
	name = 'name';
	name = 12;
	name = true;
	dynamic name;
	if(name is String){
		stringmethod
	}
	if(name is int){
		intmethod
	}
}
```

### 1.3 Nullable Variables
- null safety
	- 개발자가 null 값을 참조할 수 없도록함.
	- null을 참조할 경우 RuntimeError가 발생하기 때문.
```dart
void main() {
	String? name = 'name';
	name = null;
	name?.isNotEmpty;
	if(name != null) {
		name.isNotEmpty
	}
}

```
- 기본적으로 모든 변수는 non-Nullable 이다. 변수선언시 ?를 추가하면 null이 될 수도 있음을 명시한다.

### 1.4 Final Variables

```dart
void main() {
	final name = 'name';
	// 상수값 선언
}
```

### 1.5 Late Variables
```dart
void main() {
	late final String name;
	// do something, go to api
	name = 'name';
}
```
- late는 초기 변수 선언시에 데이터 없이 변수를 선언할 수 있게 해줌.

### 1.6 Constant Variables
- js 와 ts의 const와 final은 매우 유사함
- dart 에서의 const는 compile-time constant를 만들어 줌.
- const 는 컴파일 이전에 정해진 상수값. (앱스토어에 올리기 이전에 정하는 값)
```dart
void main() {
	const max_allowed_price = 120;
}
```

### 1.7 Recap
```dart
void main() {
	in i = 12;
	var name = 'name';
	i = 1212
	name = 'update_name';
	final name = 'name';
	dynamic name;
	name = '122';
	name = 12;
	name = true;
}
```
- var를 많이 사용하는것을 권장함.
	- 컴파일러가 타입을 추론하기 때문.
- 타입을 선언하는 것은 class나 property에서 사용할 때 권장함.