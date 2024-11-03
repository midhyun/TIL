import java.io.*;
import java.util.*;

public class BOJ_17071 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Mentoring/랜덤코딩디펜스/BOJ_17071.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[][] visited = new int[500001][2];

        Queue<Integer> q = new LinkedList<>();
        q.add(n);
        visited[n][0] = 1;
        int time = 0;
        if (n == k) {
            System.out.println(0);
            return;
        }

        while (!q.isEmpty()) {
            time++;
            k += time;
            if (k > 500000) {
                System.out.println(-1);
                break;
            }

            for (int i = 0, size = q.size(); i < size; i++) {
                Integer cur = q.poll();
                if (cur == null) continue;

                int next = cur + 1;
                if (next <= 500000 && visited[next][time % 2] == 0) {
                    visited[next][time % 2] = time;
                    q.add(next);
                }

                next = cur - 1;
                if (next >= 0 && visited[next][time % 2] == 0) {
                    visited[next][time % 2] = time;
                    q.add(next);
                }

                next = cur * 2;
                if (next <= 500000 && visited[next][time % 2] == 0) {
                    visited[next][time % 2] = time;
                    q.add(next);
                }
            }

            if (visited[k][time % 2] != 0 && visited[k][time % 2] <= time) {
                System.out.println(time);
                return;
            }
        }
    }
}