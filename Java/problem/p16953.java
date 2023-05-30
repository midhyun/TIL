package problem;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

/**
 * p16953
 */
public class p16953 {
    static long A, B;
    static int cnt = 0;

    static int bfs() {
        Queue<Long> q = new LinkedList<>();
        q.offer(A);
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                long v = q.poll();
                if (v == B) {
                    return cnt + 1;
                } else if (v > B) {
                    continue;
                }

                if (v*2 <= B) {
                    q.offer(v*2);
                }
                
                if (v * 10 + 1 <= B) {
                    q.offer(v * 10 + 1);
                }
            }
            cnt++;
            
        }
        return -1;
    }
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("problem/p16953.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String a = br.readLine();
        StringTokenizer bt = new StringTokenizer(a, " ");
        br.close();

        A = Long.parseLong(bt.nextToken());
        B = Long.parseLong(bt.nextToken());
       
        System.out.println(bfs());


    }
    
}