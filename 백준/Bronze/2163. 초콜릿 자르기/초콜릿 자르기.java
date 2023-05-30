import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String a = br.readLine();
        StringTokenizer at = new StringTokenizer(a, " ");
        br.close();
        int N = Integer.parseInt(at.nextToken());
        int M = Integer.parseInt(at.nextToken());
        
        int result = (N*M) - 1;
        System.out.println(result);



        

    }
    
}
