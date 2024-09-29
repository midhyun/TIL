import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    private static final int MOD = 1000000007;
    static long[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        dp = new long[1000001][2];
        
        System.out.println(findCase(N));

        }

    private static long findCase(int x) {

        dp[0][0] = 0;
        dp[1][0] = 2;
        dp[2][0] = 7;
        dp[2][1] = 1;

        for (int i = 3; i <= x; i++) {
            dp[i][1] = (dp[i-1][1] + dp[i-3][0]) % MOD;
            dp[i][0] = (2 * dp[i-1][0] + 3* dp[i-2][0] + 2 * dp[i][1]) % MOD;
        }

        return dp[x][0];

    }

}
