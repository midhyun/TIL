import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Long result = 0L;
        ArrayList<Integer> list = new ArrayList<>();
        list.add(Integer.parseInt(br.readLine()));
        for (int i = 1; i < N; i++) {
            int cur = Integer.parseInt(br.readLine());
            while (!list.isEmpty()) {
                int lastIdx = list.size()-1;
                if (cur >= list.get(lastIdx)) {
                    list.remove(lastIdx);
                } else {
                    break;
                }
            }
            result += list.size();
            list.add(cur);
        };
        System.out.println(result);
    }
}
