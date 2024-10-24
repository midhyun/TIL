import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static int N, M;
    static char[][] graph;
    static boolean[][] visited;
    static int[][] status;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        N = Integer.parseInt(input[0]);
        M = Integer.parseInt(input[1]);
        graph = new char[N][M];
        visited = new boolean[N][M];
        status = new int[N][M];
        for (int i = 0; i < N; i++) {
            graph[i] = br.readLine().toCharArray();
        }

//        for (int i = 0; i < N; i++) {
//            String line = br.readLine();
//            for (int j = 0; j < M; j++) {
//                graph[i][j] = line.charAt(j);
//            }
//        }

        int result = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (status[i][j] == 0) {
                    dfs(i, j);
                }
            }
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (status[i][j] == 2) {
                    result++;
                }
            }
        }
        System.out.println(result);
    }

    static boolean dfs(int y, int x) {
        // 갇힘경로
        if (visited[y][x] && (status[y][x] == 1 || status[y][x] == 0)) {
            return false;
        // 탈출경로
        } else if (visited[y][x] && status[y][x] == 2) {
            return true;
        }
        visited[y][x] = true;
        int ny = y;
        int nx = x;
        switch (graph[y][x]) {
            case 'U':
                ny--;
                break;
            case 'D':
                ny++;
                break;
            case 'L':
                nx--;
                break;
            case 'R':
                nx++;
                break;
        }

        if (ny < 0 || nx < 0 || ny >= N || nx >= M) {
            status[y][x] = 2;
            return true;
        }


        if (dfs(ny, nx)) {
            status[y][x] = 2;
            return true;
        } else {
            status[y][x] = 1;
            return false;
        }
    }
}
