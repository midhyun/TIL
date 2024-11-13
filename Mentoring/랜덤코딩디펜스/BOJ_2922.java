import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_2922 {
    static int len;
    static Long result;
    static final String isVowel = "AEIOU";
    static final String isConsonants = "BCDFGHJKMNPQRSTVWXYZ";

    // 즐거운 단어: 자음, 모음이 연속으로 3번 나오지 않으며 L이 포함되는 단어
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Mentoring/랜덤코딩디펜스/BOJ_2922.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder(br.readLine());
        len = sb.length();
        for (int i = 0; i < len; i++) {
            if (isVowel.indexOf(sb.charAt(i)) != -1) {
                sb.setCharAt(i, 'V');
            } else if (isConsonants.indexOf(sb.charAt(i)) != -1) {
                sb.setCharAt(i, 'C');
            } else if (sb.charAt(i) == 'L') {
                sb.setCharAt(i, 'L');
            }
        }
        result = 0L;
        backTracking(sb, 0, 0, 0, 1L);
        System.out.println(result);
    }
    // 자음 consonant 모음 vowel
    // 즐거운 단어를 만들 수 있는 경우의 수를 백트래킹으로 찾는다.
    public static void backTracking(StringBuilder sb, int idx, int vow, int cons, Long caseNum) {
        if (idx == len) {
            if (sb.indexOf("L") != -1) {
                result += caseNum;
            }
            return;
        }

        if (sb.charAt(idx) == '_') {
            if (vow < 2) {
                sb.setCharAt(idx, 'V');
                backTracking(sb, idx+1, vow+1, 0, caseNum*5);
                sb.setCharAt(idx, '_');
            }
            if (cons < 2) {
                sb.setCharAt(idx, 'C');
                backTracking(sb, idx+1, 0, cons+1, caseNum*20);
                sb.setCharAt(idx, '_');
            }
            if (cons < 2) {
                sb.setCharAt(idx, 'L');
                backTracking(sb, idx+1, 0, cons+1, caseNum);
                sb.setCharAt(idx, '_');
            }
        } else {
            if (sb.charAt(idx) == 'V') {
                if (vow < 2) {
                    backTracking(sb, idx+1, vow+1, 0, caseNum);
                }
            } else {
                if (cons < 2) {
                    backTracking(sb, idx+1, 0, cons+1, caseNum);
                }
            }
        }
    }
}
