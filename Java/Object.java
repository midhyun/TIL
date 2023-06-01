import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

interface Mineral {
    int addValue();
}

class Gold implements Mineral{
    public int addValue() {
        return 100;
    }
}
class Silver implements Mineral{
    public int addValue() {
        return 90;
    }
}
class Bronze implements Mineral{
    public int addValue() {
        return 80;
    }
}

class MineralCalculator {
    int value = 0;

    public void add(Mineral mineral) {
        this.value += mineral.addValue();
    }

    public int getValue() {
        return this.value;
    }
}

class Calculator {
    int value;
    int result = 0;

    Calculator() {
        this.value = 0;
    }

    void add(int val) {
        this.value += val;
    }

    void minus(int val) {
        this.value -= val;
    }
    
    int getValue() {
        return this.value;
    }

    boolean isOdd(int val) {
        return (val%2 == 1);
    }

    int avg(int[] data) {
        int result = 0;
        for (int num : data) {
            result += num;
        }

        return result / data.length;
    }

    int avg(ArrayList<Integer> data) {
        int total = 0;
        for (int num : data) {
            total += num;
        }
        return total / data.size();
    }
}

class MaxLimitCalculator extends Calculator {
    int limit;

    MaxLimitCalculator(int limit) {
        this.limit = limit;
    }

    int getValue() {
        if (this.value > this.limit) {
            return this.limit;
        } else {
            return this.value;
        }
    }
    
    void add(int val) {
        this.value += val;
        if (this.value > this.limit) {
            this.value = this.limit;
        }
    }
    
}
// 인터페이스는 인터페이스의 메서드를 반드시 구현해야 하는 "강제성"을 갖는다.
abstract class Predator extends Animal {
    abstract String getFood();

    void printFood() {
        System.out.printf("my food is %s\n", getFood());
    }

    static int LEG_COUNT = 4;

    static int speed() {
        return LEG_COUNT * 30;
    }
}

interface Barkable {
    void bark();
}

class Animal {
    String name;

    public void setName(String name) {
        this.name = name;
    }
}

class Tiger extends Predator implements Barkable {
    public String getFood() { // 인터페이스의 메서드는 항상 public으로 구현해야함.
        return "apple";
    }

    public void bark() {
        System.out.println("어흥");
    }
}

class Lion extends Predator implements Barkable {
    public String getFood() {
        return "banana";
    }

    public void bark() {
        System.out.println("으르렁");
    }
}

class Zookeeper {
    void feed(Predator predator) {
        System.out.println("feed "+predator.getFood());
    }
}

class Bouncer {
    void barkAnimal(Barkable animal) {
        animal.bark();
    }
}

class Dog extends Animal { // Animal 클래스를 상속한다.
    Dog () {

    }

    void sleep() {
        System.out.println(this.name+" zzz");
    }
}

class HouseDog extends Dog {
    HouseDog() {

    }
    HouseDog(String name) {
        this.setName(name);
    }

    void sleep() {
        System.out.println(this.name+" zzz in house");
    }

    void sleep(int hour) {
        System.out.println(this.name+" zzz in house for " + hour + "hours");
    }
}

class Updater {
    void update(Counter counter) {
        counter.count++;
    }
}

class Counter {
    int count = 0; // 객체변수
}

public class Object {

    int x;

    int sum(int a, int b) {
        return a + b;
    }

    void varTest(Object object) {
        object.x++;
    }
    public static void main(String[] args) {
        /*
         * 객체지향 프로그래밍이란?
         * 계산기의 각 연산모듈로 비유한다.
         * 
         */
        Calculator cal1 = new Calculator();
        Calculator cal2 = new Calculator();

        // System.out.println(cal1.add(3));
        // System.out.println(cal1.add(3));
        // System.out.println(cal2.add(4));
        // System.out.println(cal2.add(4));

        // new 는 객체를 생성할 때 사용하는 키워드이다.
        // cat은 Animal의 인스턴스이다. cat은 객체이다.
        Animal cat = new Animal();
        
        cat.setName("boby");
        cat.name = "boby";
                
        // Animal dog = new Animal();
        // dog.setName("happy");

        System.out.println(cat.name);
        // System.out.println(dog.name);

        int a = 3;
        int b = 4;

        Object object = new Object();
        int c = object.sum(a, b);
        System.out.println(c);

        a = 1;
        System.out.println(a);
        object.x = 1;
        object.varTest(object);
        System.out.println(object.x);

        // Call by value
        Counter myCounter = new Counter();
        System.out.println("Before update:"+myCounter.count);
        Updater myUpdater = new Updater();
        myUpdater.update(myCounter);
        System.out.println("after update:"+myCounter.count);
        
        // 상속
        // Dog dog = new Dog();
        // dog.setName("poppy");
        // System.out.println(dog.name);
        // dog.sleep();

        // Dog 객체를 Animal 자료형으로 사용할 경우, Dog클래스에만 존재하는 메서드를 사용할 수 없다.
        Animal dog = new Dog(); // Dog is a Animal
        // Dog dog1 = new Animal(); 컴파일 에러가 발생.

        /* Object 클래스
         * 자바에서 만드는 모든 클래스는 Object 클래스를 상속받는다.
         */

        // 메서드 오버라이딩 (Method overriding)
        // HouseDog houseDog = new HouseDog();
        // houseDog.setName("happy");
        // houseDog.sleep();
        

        // 메서드 오버로딩 (Method overloading)
        // houseDog.sleep(3);

        // 생성자 (Constructor): 메서드명이 클래스명과 동일하고 리턴 자료형을 정의 하지 않는 메서드
        // 생성자의 규칙
        // 1. 클래스명과 메서드명이 동일하다.
        // 2. 리턴타입을 정의하지 않는다. (void도 사용하지 않는다.)
        HouseDog houseDog = new HouseDog("happy");
        HouseDog nonameDog = new HouseDog();
        System.out.println(houseDog.name);
        System.out.println(nonameDog.name);

        Zookeeper zooKeeper = new Zookeeper();
        Tiger tiger = new Tiger();
        Lion lion = new Lion();
        zooKeeper.feed(tiger);
        zooKeeper.feed(lion);

        Bouncer bouncer = new Bouncer();
        bouncer.barkAnimal(lion);
        bouncer.barkAnimal(tiger);

        // 1. UpgradeCalculator
        // Calculator cal = new Calculator();
        // cal.add(10);
        // cal.minus(3);
        // System.out.println(cal.getValue());

        // 2. MaxLimitCalculator
        // MaxLimitCalculator cal = new MaxLimitCalculator(100);
        // cal.add(50);
        // cal.add(60);
        // System.out.println(cal.getValue());


        // 3. 홀수 짝수 판별하기
        Calculator cal = new Calculator();
        System.out.println(cal.isOdd(3));
        System.out.println(cal.isOdd(4));

        // 4. 평균값을 구하는 메서드
        int[] data = {1, 3, 5, 7, 9};
        int result = cal.avg(data);
        System.out.println(result);


        // 5. 리스트와 객체
        // 얕은복사와 깊은복사

        // 6. 생성자와 초깃값
        // value의 초깃값이 null 이므로 value = 0으로 초기화 한다.

        // 7. 인터페이스 사용하기
        MineralCalculator cal_m = new MineralCalculator();
        cal_m.add(new Gold());
        cal_m.add(new Silver());
        cal_m.add(new Bronze());
        System.out.println(cal_m.getValue());

        // 8. 오류찾기
        // 4번: Animal은 Dog의 부모클래스이므로 Dog 자료형이 될 수 없다.

        // 9. 오류찾기2
        // 2번 : Animal 자료형은 bark()메서드를 실행할 수없음.
        // 5번 : Predator 인터페이스는 Animal의 hello()메서드를 실행 할 수 없음.

        ArrayList<Integer> testa = new ArrayList<>(Arrays.asList(1,2,3));
        ArrayList<Integer> testb = testa;
        testa.add(4);
        System.out.println(testa==testb);

        
    }
    



}