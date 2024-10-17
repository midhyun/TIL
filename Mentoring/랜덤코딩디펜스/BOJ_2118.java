import java.io.*;

public class BOJ_2118 {

    static int N, left, right, leftDistance, rightDistance;
    static int result;
    static int[] arr;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Mentoring/랜덤코딩디펜스/BOJ_2118.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N];
        arr[0] = Integer.parseInt(br.readLine());

        for (int i = 1; i < N; i++) {
            arr[i] = arr[i-1] + Integer.parseInt(br.readLine());
        }
        result = left = right = 0;
        while(right < N && left <= right) {
            leftDistance = getLeft(left, right, arr);
            rightDistance = getRight(leftDistance, arr);

            if (leftDistance < rightDistance) {
                right++;
            } else {
                left++;
            }
            result = Math.max(result, Math.min(leftDistance, rightDistance));
        }


        System.out.println(result);
    }

    public static int getLeft(int start, int end, int[] arr) {
        return arr[end] - arr[start];
    }

    public static int getRight(int leftDistance, int[] arr) {
        return arr[N-1] - leftDistance;
    }
}
