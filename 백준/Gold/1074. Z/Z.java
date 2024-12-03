import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N, r, c;
    static Long cnt = 0L;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        solve(N, 0, 0);
    }

    static void solve(int n, int y, int x) {
        if (n == 0) {
            if (x == c && y == r) {
                System.out.println(cnt);
                System.exit(0);
            }
            cnt++;
            return;
        }
        int half = 1 << (n - 1);

        if (r < y + half && c < x + half) {
            solve(n-1, y, x);
        } else if ( r < y + half && c >= x + half) {
            cnt += (long) half * half;
            solve(n - 1, y, x + half);
        } else if ( r >= y + half && c < x + half) {
            cnt += 2L * half * half;
            solve(n - 1, y + half, x);
        } else if ( r >= y + half && c >= x + half) {
            cnt += 3L * half * half;
            solve(n - 1, y + half, x + half);
        }
    }
}
