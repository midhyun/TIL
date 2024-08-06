import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class RoofTopDeco {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Mentoring/랜덤코딩디펜스/6198_옥상정원꾸미기.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Long result = 0L;
        ArrayList<Integer> stack = new ArrayList<>();
        stack.add(Integer.parseInt(br.readLine()));
        for (int i = 1; i < N; i++) {
            int cur = Integer.parseInt(br.readLine());
            while (!stack.isEmpty()) {
                int lastIdx = stack.size() - 1;
                if (cur >= stack.get(lastIdx)) {
                    stack.remove(lastIdx);
                } else {
                    break;
                }
            }
            result += stack.size();
            stack.add(cur);
        };
        System.out.println(result);
    }
}
