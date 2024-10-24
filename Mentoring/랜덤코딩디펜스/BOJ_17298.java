import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class BOJ_17298 {

    static int N;
    static int[] A, NGE;
    static String[] input;
    static List<Integer> stack;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Mentoring/랜덤코딩디펜스/BOJ_17298.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        A = new int[N];
        NGE = new int[N];
        stack = new ArrayList<>();
        input = br.readLine().split(" ");
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(input[i]);
        }

        for (int i = N-1; i >= 0; i--) {
            while (!stack.isEmpty() && stack.get(stack.size()-1) <= A[i]) {
                stack.remove(stack.size()-1);
            }
            if (stack.isEmpty()) {
                NGE[i] = -1;
            } else {
                NGE[i] = stack.get(stack.size()-1);
            }
            stack.add(A[i]);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            sb.append(NGE[i]).append(" ");
        }
        System.out.println(sb);
    }
}
