import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_14719 {

    static int[][] graph;
    static int H, W;
    static boolean isOpen = false;
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Mentoring/랜덤코딩디펜스/BOJ_14719.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        H = Integer.parseInt(st.nextToken());
        W = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        graph = new int[H][W];
        for (int j = 0; j < W; j++) {
            int height = Integer.parseInt(st.nextToken());
            for (int i = 0; i < height; i++) {
                graph[i][j] = 1;
            }
        }

        int answer = 0;
        for (int i = 0; i < H; i++) {
            isOpen = false;
            int temp = 0;
            for (int j = 0; j < W; j++) {
                if (graph[i][j] == 1) {
                    if (isOpen) {
                        answer += temp;
                    } else {
                        isOpen = true;
                    }
                    temp = 0;
                } else {
                    if (isOpen) {
                        temp++;
                    }
                }
            }
        }

        System.out.println(answer);


    }
}
