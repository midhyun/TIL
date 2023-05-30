/**
 * ControlCode
 */
public class ControlCode {
    public static void main(String[] args) {
        // and(&&), or(||), not(!)
        int month = 8;
        String monthString = "";
        switch (month) {
            case 1: monthString = "January";
                    break;
            case 2: monthString = "February";
                    break;
            case 3: monthString = "March";
                    break;
            case 4:  monthString = "April";
                    break;
            case 5:  monthString = "May";
                    break;
            case 6:  monthString = "June";
                    break;
            case 7:  monthString = "July";
                    break;
            case 8:  monthString = "August";
                    break;
            case 9:  monthString = "September";
                    break;
            case 10: monthString = "October";
                    break;
            case 11: monthString = "November";
                    break;
            case 12: monthString = "December";
                    break;
            default: monthString = "Invalid month";
                    break;

        }
        System.out.println(monthString);

        int treeHit = 0;
        while (treeHit < 10) {
            treeHit += 1;
            System.out.println("나무를 " + treeHit + "번 찍었습니다.");
            if (treeHit == 10) {
                System.out.println("나무 넘어갑니다.");;
            }
        }
        String[] numbers = {"one", "two", "three"};
        for (int i=0; i<numbers.length; i++) {
            System.out.println(numbers[i]);
        }

        int[] marks = {90, 25, 67, 45, 80};
        for (int i=0; i<marks.length; i++) {
            if (marks[i] >= 60) {
                System.out.println((i+1) + "번 학생은 합격입니다.");
            } else {
                System.out.println((i+1) + "번 학생은 불합격입니다.");
            }
        }

        for (int i=0; i<marks.length; i++) {
            if (marks[i] >= 60) {
                System.out.println((i+1) + "번 학생 축하합니다. 합격입니다.");
            } else {
                continue;
            }
        }

        for (String number: numbers) {
            System.out.println(number);
        }

        // 연습문제
        // 1. 조건문의 참과 거짓
        // ans = "anywhere"

        // 2. 3의 배수의 합
        int i = 0;
        int result = 0;
        while (i <= 1000) {
            i++;
            if (i%3 == 0) {
                result += i;
            }
        }
        System.out.println(result);

        // 3. 별 표시하기
        for (i = 0; i < 6; i++) {
            for (int j = 0; j < i; j++) {
                System.out.print("*");
            }
            System.out.println("");
        }

        // 4. 1부터 100까지 출력하기.
        for (i = 0; i < 101; i++) {
            System.out.println(i);
        }

        // 5. 평균점수 구하기
        int[] marks1 = {70, 60, 55, 75, 95, 90, 80, 80, 85, 100};
        int total = 0;
        for (int mark: marks1) {
            total += mark;
        }
        System.out.println((float) total/marks1.length);
        


    }
    
}
