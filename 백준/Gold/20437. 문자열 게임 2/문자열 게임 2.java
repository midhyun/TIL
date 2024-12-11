import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static int T, K;
    static int min, max;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());

        // 테스트 케이스만큼 반복
        for (int t = 0; t < T; t++) {
            String str = br.readLine();
            K = Integer.parseInt(br.readLine());
            List<List<Integer>> list = new ArrayList<>(); //2차원 리스트 선언
            for (int i = 0; i < 26; i++) {
                list.add(new ArrayList<>());
            }

            for (int i = 0; i < str.length(); i++) {
                list.get(str.charAt(i) - 'a').add(i);
            }

            min = Integer.MAX_VALUE;
            max = 0;

            for (int i = 0; i < 26; i++) {
                if (list.get(i).size() < K) continue;

                int size = list.get(i).size();
                for (int j = 0; j <= size - K; j++) {
                    min = Math.min(min, list.get(i).get(j + K - 1) - list.get(i).get(j) + 1);
                    max = Math.max(max, list.get(i).get(j + K - 1) - list.get(i).get(j) + 1);
                }
            }
            if (min == Integer.MAX_VALUE || max == 0) {
                System.out.println(-1);
                continue;
            }
            System.out.println(min + " " + max);

        }
    }
}
