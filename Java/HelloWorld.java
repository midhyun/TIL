import java.awt.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;

import javax.lang.model.type.IntersectionType;

/**
 * HelloWorld
 */
public class HelloWorld {

    /**
     * @param args
     */
    public static void main(String[] args) {
        int a = 1;
        String b = "Hello Java";
        /*
        변수명은 숫자로 시작 할 수 없다.
        underscore(_) 와 $ 문자 이외의 특수문자는 사용할 수 없다.
        자바의 키워드(예약어)는 변수명으로 사용할 수 없다. (ex: int, class, return 등)
        */
        StringBuffer sb;
        List myList;

        // 자바에서의 자료형

        // 정수 (default = int), long 을 사용할때는 'L'을 접미사로 붙여야한다.
        int age = 10;
        long countOfStar = 8765827384923849L;

        // 실수 (default = double), float 을 사용할때는 'F'를 접미사로 붙여야 한다.
        float pi = 3.14F;
        double morePi = 3.14159265358979323846;
        // 실수는 과학적 지수 표현식으로 다음과 같이 사용할 수 있다.
        double d1 = 123.4;
        double d2 = 1.234e2;
        // d1 == d2 이다 123.4 == 1.234*10^2

        // 8진수와 16진수는 int 자료형을 사용하여 표시한다.
        int octal = 023;
        int hex = 0xc;

        // 숫자연산
        int a2 = 10;
        int b2 = 5;
        System.out.println(a2+b2); // + - * / 4칙연산
        System.out.println(7%4); // 나머지 연산 ans = 1

        // 증감연산
        int i = 0;
        int j = 10;
        i++;
        j++;
        System.out.println(i++); // i를 출력후 증감 연산 실행
        System.out.println(++j); // 증감연산 후 j를 출력

        // 문자 (char) 한 개의 문자 값에 대한 자료형, 문자값을 '' 작은따옴표로 감싸야함
        char a1 = 'a';

        // 문자열 (String), 문자들로 구성된 문장을 의미함.
        String a3 = "Happy Java";
        String b3 = "a";
        String a4 = new String("Happy Java"); // new 키워드는 객체를 만들때 사용함.
        /*
         * 리터럴 표기
         * String a = "happy java" 와 String b = new String("happy java")에서
         * a, b 변수는 동일한 문자열 값을 갖게 되지만 완전히 동일하지는 않다.
         * 첫번째 방식은 리터럴표기라고 하는데 객체 생성없이 고정된 값을 그대로 대입하는 방법을 말한다.
         * 좀 더 자세히 알아보면, 리터럴 표기법은 "happy java"라는 문자열을 JVM의 intern pool 이라는
         * 메모리 공간에 저장하고 다음에 다시 동일한 문자열이 선언될때는 cache 된 문자열을
         * 리턴한다. 이와는 달리 두번째 방식은 항상 새로운 String 객체를 만든다.
         */

        // 원시(primitive) 자료형 (int, long, double, float, bollean, char)
        
        // 문자열 내장 메서드
        String a5 = "hello java";
        String b5 = new String("hello java");
        System.out.println(a5.equals(b5)); // true 같은 값이므로
        System.out.println(a5 == b5); // false 서로 다른 객체이므로
        System.out.println(a5.indexOf("java")); // 6출력: 문자열의 시작위치
        System.out.println(a5.contains("java")); // true: 특정 문자열 포함여부
        System.out.println(a5.charAt(6)); // "j" 출력: 해당 인덱스의 값
        System.out.println(a5.replaceAll("java", "World")); // hello World 출력
        System.out.println(a5.substring(0, 4)); // 문자열 슬라이싱
        System.out.println(a5.toUpperCase()); // 모두 대문자로 변경
        String a6 = "a:b:c:d";
        System.out.println(a6.split(":")); // {"a", "b", "c", "d"} 배열 출력
        System.out.println(String.format("I eat %d apples", 3)); // "I eat 3 apples"
        System.out.println(String.format("I eat %s apples", "five")); // "I eat five apples"

        // StringBuffer 문자열을 추가하거나 변경할 때 주로 사용하는 자료형.
        // String은 + 연산을 할때 마다 새로운 객체를 생성함, StringBuffer는 muatble 함
        // 문자열의 추가나 변경 등의 작업이 많을 경우에는 StringBuffer, 없을 경우에는 String을 사용하는 것이 유리하다.

        // 리스트 (List)
        
        ArrayList pitches = new ArrayList();
        pitches.add("138");
        pitches.add("129");
        pitches.add("142");
        pitches.add(1, "133");
        System.out.println(pitches);
        System.out.println(pitches.get(1)); // 해당 인덱스의 값 출력
        System.out.println(pitches.size()); // 리스트 길이 출력
        System.out.println(pitches.contains("142")); // true
        System.out.println(pitches.remove("129")); // 객체 삭제 > 결과출력 true or false
        System.out.println(pitches.remove(0)); // 인덱스 삭제 > 삭제된 값 리턴

        // 제네릭스 Generics > 어려운내용이므로 정석 때 공부할 것
        ArrayList<String> pitches1 = new ArrayList<String>(); // 제네릭스
        ArrayList<String> pitches2 = new ArrayList<>(); // 선호되는 방식
        pitches.sort(Comparator.naturalOrder());
        System.out.println(pitches);
        pitches.sort(Comparator.reverseOrder());
        System.out.println(pitches);


        // 맵 (Map) 자료형: 파이썬의 딕셔너리
        // 해시 맵 (HashMap): 자바의 맵중 가장 기본적인 맵
        HashMap<String, String> map = new HashMap<>();
        map.put("people", "사람");
        map.put("baseball", "야구");
        System.out.println(map.get("people"));
        System.out.println(map.getOrDefault("java", "자바"));
        System.out.println(map.containsKey("people"));
        System.out.println(map.remove("people")); // 삭제 후 삭제한 값 리턴
        System.out.println(map.size());
        System.out.println(map.keySet()); // Map의 모든 Key를 모아서 Set 자료형으로 리턴
        // LinkedHashMap: 입력된 순서대로 데이터를 저장
        // TreeMap: 입력된 key의 오름차순 순서로 데이터를 저장

        // 집합 (Set): 집합과 관련된 것을 쉽게 처리하기 위해 만든 자료형
        HashSet<String> set = new HashSet<>(Arrays.asList("H", "e", "l", "l", "o"));
        System.out.println(set); // [e, H, l, o] 출력
        /*
         * Set 자료형에는 HashSet, TreeSet, LinkedHashSet 등의 Set 인터페이스를 구현한
         * 자료형이 있다. 여기서 말하는 Set 자료형은 인터페이스인데 인터페이스에 대해서는
         * 뒤에서 자세히 다루도록 한다.
         */

        // 중복을 허용하지 않음, 순서가 없음
        // 교집합, 합집합, 차집합 구하기!
        HashSet<Integer> s1 = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5, 6));
        HashSet<Integer> s2 = new HashSet<>(Arrays.asList(4, 5, 6, 7, 8, 9));
        System.out.println(s1);
        System.out.println(s2);

        HashSet<Integer> interSection = new HashSet<>(s1);
        interSection.retainAll(s2); // 교집합
        System.out.println(interSection); 
        
        HashSet<Integer> union = new HashSet<>(s1);
        union.addAll(s2); // 합집합
        System.out.println(union);

        HashSet<Integer> substract = new HashSet<>(s1);
        substract.removeAll(s2);
        System.out.println(substract);

        set.add("Jump"); // 값 추가
        set.add("To");
        set.add("Java");
        System.out.println(set);

        set.addAll(Arrays.asList("Python", "Django")); // 여러 값 추가
        set.remove("Jump"); // 값 제거
        System.out.println(set);

        /*
         * TreeSet과 LinkedHashSet
         * Set 자료형은 순서가 없다는 특징이 있다. 하지만 가끔은 Set에 입력된 순서대로
         * 데이터를 가져오고 싶은 경우도 있고 때로는 오름차순으로 정렬된 데이터를 가져오고
         * 싶을 수도 있을 것이다. 이런 경우에는 TreeSet과 LinkedHashSet을 사용한다.
         * LinkedHashSet - 입력한 순서대로 값을 정렬하여 저장하는 특징
         * TreeSet - 오름차순으로 값을 정렬하여 저장하는 특징
         */

        // 상수집합 (Enum)
        System.out.println(CoffeType.AMERICANO);
        for(CoffeType type: CoffeType.values()) {
            System.out.println(type);
        }

        // 형 변환
        String num = "123";
        int n = Integer.parseInt(num);
        System.out.println(n);
        num = "" + n;
        System.out.println(num);
        num = "123.456";
        double d = Double.parseDouble(num);
        System.out.println(d);
        int n1 = (int) d;
        System.out.println(n1);

        final int n2 = 123;
        System.out.println(n2);
        
        // 연습문제
        // 1. 평균점수 구하기
        int 국어 = 80;
        int 영어 = 75;
        int 수학 = 55;
        int 평균점수;
        평균점수 = (국어 + 영어 + 수학) / 3;
        System.out.println(평균점수);

        //2. 홀수 짝수 판별
        int isodd = 13;
        if (isodd % 2 == 0) {
            System.out.println("짝수");
        } else {
            System.out.println("홀수");
        }

        //3. 주민등록번호 나누기
        String registration_num = "881120-1068234";
        String YMD = registration_num.substring(0, 6);
        String BRN = registration_num.substring(7, 14);
        System.out.println(YMD);
        System.out.println(BRN);

        //4. 주민등록번호 인덱싱
        System.out.println(registration_num.charAt(7));

        //5. 문자열 바꾸기
        String a7 = "a:b:c:d";
        a7.replace(":", "#");
        System.out.println(a7.replace(":", "#"));

        //6. 리스트 역순 정렬하기
        ArrayList<Integer> myList2 = new ArrayList<>(Arrays.asList(1, 3, 5, 4, 2));
        myList2.sort(Comparator.reverseOrder());
        System.out.println(myList2);

        //7. 리스트를 문자열로 만들기
        ArrayList<String> myList3 = new ArrayList<>(Arrays.asList("Life", "is", "too", "short"));
        System.out.println(String.join(" ", myList3));

        //8. 맵에서 값 추출하기
        HashMap<String, Integer> grade = new HashMap<>();
        grade.put("A", 90);
        grade.put("B", 80);
        grade.put("C", 70);
        System.out.println(grade.remove("B"));
        System.out.println(grade);

        //9. 중복 숫자 제거하기
        ArrayList<Integer> numbers = new ArrayList<>(Arrays.asList(1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5));
        HashSet<Integer> numbersSet = new HashSet<>(numbers);
        ArrayList<Integer> numbers2 = new ArrayList<>(numbersSet);
        System.out.println(numbers2);

        //10. 매직넘버 제거하기
        printCoffeePrice(CoffeType.AMERICANO);
        printCoffeePrice(CoffeType.CAFE_LATTE);

    }

    enum CoffeType {
        AMERICANO,
        ICE_AMERICANO,
        CAFE_LATTE
     };

    static void printCoffeePrice(CoffeType type) {
        HashMap<CoffeType, Integer> priceMap = new HashMap<>();
        priceMap.put(CoffeType.AMERICANO, 3000);  // 1: 아메리카노
        priceMap.put(CoffeType.ICE_AMERICANO, 4000);  // 2: 아이스 아메리카노
        priceMap.put(CoffeType.CAFE_LATTE, 5000);  // 3: 카페라떼
        int price = priceMap.get(type);
        System.out.println(String.format("가격은 %d원 입니다.", price));
    }

}