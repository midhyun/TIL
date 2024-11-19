import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    static String[] map;
    static HashMap<String, Integer> mapCount;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        map = new String[N];
        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            map[i] = str;
        }

        int K = Integer.parseInt(br.readLine());
        mapCount = new HashMap<>();
        int max = 0;

        for (int i = 0; i < N; i++) {
            String str = map[i];
            if (mapCount.containsKey(str)) {
                mapCount.put(str, mapCount.get(str) + 1);
            } else {
                long count = str.chars().filter(ch -> ch == '0').count();
                if (count <= K && (K - count) % 2 == 0) {
                    mapCount.put(str, 1);
                }
            }
        }

        for (String key : mapCount.keySet()) {
            Integer count = mapCount.get(key);
            max = Math.max(max, count);
        }

        System.out.println(max);




    }
}
