import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class swealgo2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());
            int Q = Integer.parseInt(st.nextToken());

            int[][] graph = new int[N][M];
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < M; j++) {
                    graph[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            Set<Integer> safe = new HashSet<>();
            int[] check_i = new int[N];
            int[] check_j = new int[M];

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    check_i[i] = Math.max(check_i[i], graph[i][j]);
                    check_j[j] = Math.max(check_j[j], graph[i][j]);
                }
            }

            for (int i = 0; i < N; i++) {
                for (int j = 0; j < M; j++) {
                    if (graph[i][j] == check_i[i] && graph[i][j] == check_j[j]) {
                        safe.add(graph[i][j]);
                    }
                }
            }

            int res = 0;
            for (int q = 0; q < Q; q++) {
                st = new StringTokenizer(br.readLine());
                int r = Integer.parseInt(st.nextToken()) - 1;
                int c = Integer.parseInt(st.nextToken()) - 1;
                int x = Integer.parseInt(st.nextToken());

                graph[r][c] = x;

                if (check_i[r] < x) {
                    safe.remove(check_i[r]);
                    check_i[r] = x;
                }

                if (check_j[c] < x) {
                    safe.remove(check_j[c]);
                    check_j[c] = x;
                }

                if (check_i[r] == x && check_j[c] == x) {
                    safe.add(x);
                }

                res += safe.size();
            }

            System.out.println("#" + test_case + " " + res);
        }
    }
}