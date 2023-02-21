### 2.0 Basic Data Types
- 객체 지향 언어이므로 데이터타입은 객체로 이루어져있다.
- ex) int, double 은 num 이라는 클래스를 상속받고 있다.
```dart
void main() {
	String name = 'name';
	bool alive = true;
	int age = 12;
	double money = 69.99;
	num x = 12;
	x = 1.1;
}
```

### 2.1 Lists
- list 의 객체는 `List<E>` 형태를 띄고 있음.
- collection if 는 조건에 따라 리스트의 값을 정할 수 있음.
- dart의 유용한 점은 `collection if`와 `collection for`을 지원하는 것이다. collection if를 사용하면 `존재할 수도 안할 수도 있는 요소를 가지고 올 수 있다.`
```dart
void main() {
	var numbers = [1, 2, 3, 4]; // case 1
	List<int> numbers = [1, 2, 3, 4]; // case 2
	numbers.add('string') // X
	numbers.fisrt;
	numbers.last;

	var giveMeFive = true;
	var numbers = [
	1,
	2,
	3,
	4,
	if (giveMeFive) 5 // collection if
	];
	print(numbers);
}
```

### 2.2 String Interpolation
- text에 변수를 추가하는 방법.
- $달러 기호를 붙이고 사용할 변수를 적어주면 된다.  
- 만약 무언가를 계산하고 싶다면 ${ } 형태로 적어주면 된다.
```dart
void main() {
	var name = 'name';
	var age = 10;
	var greeting = "Hello everyone, my name is $name and I'm ${age + 2}"; // name, 12
	print(greeting);
}
```