import org.w3c.dom.Node;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class avoidWatch_18428 {
    public static int N;
    public static char[][] graph;
    public static int[] dx, dy;
    public static ArrayList<int[]> stack;
    public static boolean flag = false;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Mentoring/랜덤코딩디펜스/18428.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        dx = new int[] {-1, 1, 0, 0};
        dy = new int[] {0, 0, 1, -1};
        N = Integer.parseInt(br.readLine());
        graph = new char[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                graph[i][j] = st.nextToken().charAt(0);
            }
        }
        backTracking(graph, 0);

        if (flag) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }

    public static void backTracking(char[][] graph, int depth) {
        if (depth == 3) {
            if (check(graph)){
                flag = true;
            }
            return;
        }
        if (flag) {
            return;
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (graph[i][j] == 'X') {
                    graph[i][j] = 'O';
                    backTracking(graph, depth + 1);
                    graph[i][j] = 'X';
                }
            }
        }
    }

    public static boolean check(char[][] graph) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (graph[i][j] == 'S') {
                    for (int k = 0; k < 4; k++) {
                        int nx = j + dx[k];
                        int ny = i + dy[k];
                        while (true) {
                            if (0 <= ny && ny < N && 0 <= nx && nx < N) {
                                if (graph[ny][nx] == 'T') {
                                    return false;
                                } else if (graph[ny][nx] == 'O') {
                                    break;
                                }
                            } else {
                                break;
                            }
                            nx += dx[k];
                            ny += dy[k];
                        }
                    }
                }
            }
        }
        return true;
    }
}
