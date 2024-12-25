import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_2138 {
    static int N, count0, count1, answer = Integer.MAX_VALUE;
    static String start, end;
    static boolean[] startArr0, startArr1, endArr;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Mentoring/랜덤코딩디펜스/BOJ_2138.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        startArr0 = new boolean[N];
        endArr = new boolean[N];
        start = br.readLine();
        end = br.readLine();
        for (int i = 0; i < N; i++) startArr0[i] = (start.charAt(i) - '0' != 0);
        for (int i = 0; i < N; i++) endArr[i] = (end.charAt(i) - '0' != 0);
        startArr1 = startArr0.clone();

        if (startArr0[0]) {
            switchLamp(startArr0, 0);
            count0++;
        } else {
            switchLamp(startArr1, 0);
            count1++;
        }

        for (int i = 1; i < N; i++) {
            if (startArr0[i - 1] != endArr[i - 1]) {
                switchLamp(startArr0, i);
                count0++;
            }
            if (startArr1[i - 1] != endArr[i - 1]) {
                switchLamp(startArr1, i);
                count1++;
            }
        }
        if (startArr0[N - 1] == endArr[N - 1]) {
            answer = Math.min(answer, count0);
        }
        if (startArr1[N - 1] == endArr[N - 1]) {
            answer = Math.min(answer, count1);
        }
        System.out.println(answer == Integer.MAX_VALUE ? -1 : answer);
    }

    public static void switchLamp(boolean[] arr, int idx) {
        arr[idx] = !arr[idx];
        if (idx - 1 >= 0) arr[idx - 1] = !arr[idx - 1];
        if (idx + 1 < N) arr[idx + 1] = !arr[idx + 1];
    }
}
