import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class acmicpc_11382 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Mentoring/랜덤코딩디펜스/input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str, " ");
        Long A = Long.parseLong(st.nextToken());
        Long B = Long.parseLong(st.nextToken());
        Long C = Long.parseLong(st.nextToken());

        br.close();

        sb.append(A+B+C).append('\n');
        System.out.println(sb);
    }
}
