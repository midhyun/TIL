/////////////////////////////////////////////////////////////////////////////////////////////
// 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
// 아래 표준 입출력 예제 필요시 참고하세요.
// 표준 입력 예제
// int a;
// double b;
// char g;
// String var;
// long AB;
// a = sc.nextInt();                           // int 변수 1개 입력받는 예제
// b = sc.nextDouble();                        // double 변수 1개 입력받는 예제
// g = sc.nextByte();                          // char 변수 1개 입력받는 예제
// var = sc.next();                            // 문자열 1개 입력받는 예제
// AB = sc.nextLong();                         // long 변수 1개 입력받는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
// 표준 출력 예제
// int a = 0;                            
// double b = 1.0;               
// char g = 'b';
// String var = "ABCDEFG";
// long AB = 12345678901234567L;
//System.out.println(a);                       // int 변수 1개 출력하는 예제
//System.out.println(b); 		       						 // double 변수 1개 출력하는 예제
//System.out.println(g);		       						 // char 변수 1개 출력하는 예제
//System.out.println(var);		       				   // 문자열 1개 출력하는 예제
//System.out.println(AB);		       				     // long 변수 1개 출력하는 예제
/////////////////////////////////////////////////////////////////////////////////////////////
import java.util.Scanner;
import java.io.*;
import java.util.*;
/*
   사용하는 클래스명이 Solution 이어야 하므로, 가급적 Solution.java 를 사용할 것을 권장합니다.
   이러한 상황에서도 동일하게 java Solution 명령으로 프로그램을 수행해볼 수 있습니다.
 */
class Solution
{
    static int id = 0;
    static List<Integer>[] graph;
    static long[][] cost;
    static int[] visited;
    static boolean[] onStack;
    static Stack<Integer> stack;
    static List<Set<Integer>> result;
    static long tmp;
    
	public static void main(String args[]) throws IOException
	{
		/*
		   아래의 메소드 호출은 앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
		   여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
		   이 코드를 프로그램의 처음 부분에 추가하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
		   따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 메소드를 사용하셔도 좋습니다.
		   단, 채점을 위해 코드를 제출하실 때에는 반드시 이 메소드를 지우거나 주석 처리 하셔야 합니다.
		 */
		//System.setIn(new FileInputStream("res/input.txt"));

		/*
		   표준입력 System.in 으로부터 스캐너를 만들어 데이터를 읽어옵니다.
		 */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
		/*
		   여러 개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
		*/

		for(int test_case = 1; test_case <= T; test_case++)
		{
            StringTokenizer st = new StringTokenizer(br.readLine());
            int V = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());
            visited = new int[V + 1];
            onStack = new boolean[V + 1];
            stack = new Stack<>();
            graph = new ArrayList[V + 1];
            cost = new long[V + 1][V + 1];
            for (int i = 1; i <= V; i++) {
                graph[i] = new ArrayList<Integer>();
            }
            result = new ArrayList<>();

            for (int i = 0; i < E; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                int x = Integer.parseInt(st.nextToken());
                graph[a].add(b);
                cost[a][b] = x;
            }

            for (int i = 1; i <= V; i++) {
                if (visited[i] == 0) {
                    dfs(i);
                }
            }

            long res = Long.MAX_VALUE;
            for (Set<Integer> scc : result) {
                tmp = 0;
                boolean[] visitedCost = new boolean[V + 1];
                dfsCost(scc.iterator().next(), visitedCost, scc);
				if (tmp != 0) {
                	res = Math.min(res, tmp);
                }
            }
            for (int i = 1; i <= V; i++) {
                if (cost[i][i] != 0) {
                    res = Math.min(res, cost[i][i]);
                }
            }
            if (res == Long.MAX_VALUE) {
                res = -1;
            }
            System.out.println("#" + test_case + " " + res);

		}
	}
    private static int dfs(int cur) {
        id++;
        visited[cur] = id;
        stack.push(cur);
        onStack[cur] = true;
        int parent = visited[cur];

        for (int nxt : graph[cur]) {
            if (visited[nxt] == 0) {
                parent = Math.min(parent, dfs(nxt));
            } else if (onStack[nxt]) {
                parent = Math.min(parent, visited[nxt]);
            }
        }

        if (parent == visited[cur]) {
            Set<Integer> scc = new HashSet<>();
            while (true) {
                int x = stack.pop();
                onStack[x] = false;
                scc.add(x);
                if (x == cur) {
                    break;
                }
            }

            result.add(scc);
        }

        return parent;
    }

    private static void dfsCost(int cur, boolean[] visitedCost, Set<Integer> scc) {
        for (int nxt : graph[cur]) {
            if (scc.contains(nxt) && !visitedCost[nxt]) {
                visitedCost[nxt] = true;
                tmp += cost[cur][nxt];
                dfsCost(nxt, visitedCost, scc);
            }
        }
    }
}