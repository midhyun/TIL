import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static int N;
    public static int[] numArr;
    public static boolean[] visited, answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        numArr = new int[N];
        answer = new boolean[2000001];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            numArr[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(numArr);
        int target = 0;
        for (int num: numArr) {
            if (target+1 < num) break;
            target += num;
        }
        br.close();
        System.out.println(target+1);

    }
}
