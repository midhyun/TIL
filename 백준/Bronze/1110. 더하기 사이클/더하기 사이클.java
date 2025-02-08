import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int cnt = 0;
        int newN = N;
        while (true) {
            int a = newN / 10;
            int b = newN % 10;
            int sum = a + b;
            newN = b * 10 + sum % 10;
            cnt++;
            if (newN == N) {
                System.out.println(cnt);
                break;
            }
        }
    }
}
