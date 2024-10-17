import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class BOJ_1261 {

    static class Status implements Comparable<Status> {
        int y, x, cnt;

        public Status(int y, int x, int cnt) {
            this.y = y;
            this.x = x;
            this.cnt = cnt;
        }

        @Override
        public int compareTo(Status o) {
            return Integer.compare(this.cnt, o.cnt);
        }
    }

    static int[] dy, dx;
    static int N, M;
    static int[][] map;
    static boolean[][] visited;
    static PriorityQueue<Status> pq;

    static public void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Mentoring/랜덤코딩디펜스/BOJ_1261.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        M = Integer.parseInt(input[0]);
        N = Integer.parseInt(input[1]);
        visited = new boolean[N][M];
        pq = new PriorityQueue<Status>();
        dy = new int[] {1, -1, 0, 0};
        dx = new int[] {0, 0, 1, -1};
        map = new int[N][M];
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            // python code: map[i] = list(map(int, list(line)))
            for (int j = 0; j < M; j++) {
                map[i][j] = line.charAt(j) - '0';
            }
        }
        visited[0][0] = true;
        pq.add(new Status(0, 0, 0));
        dijkstra();
    }

    static public void dijkstra() {
        while (!pq.isEmpty()) {
            Status cur = pq.poll();
            // 골인지점에 도달할 경우 종료
            if (cur.y == N - 1 && cur.x == M -1 ) {
                System.out.println(cur.cnt);
                return;
            }
            // 4방향 탐색 진행
            for (int k = 0; k < 4; k++) {
                int ny = cur.y + dy[k];
                int nx = cur.x + dx[k];

                if (ny < 0 || nx < 0 || ny >= N || nx >= M) {
                    continue;
                }

                if (!visited[ny][nx]) {
                    visited[ny][nx] = true;
                    pq.add(new Status(ny, nx, cur.cnt + map[ny][nx]));
                }
            }
        }
    }


}
