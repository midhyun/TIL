import java.io.BufferedReader;
import java.util.*;
import java.io.IOException;
import java.io.InputStreamReader;

public class StronglyConnectedComponents {
    static int id = 0;
    static List<Integer>[] graph;
    static int[][] cost;
    static int[] visited;
    static boolean[] onStack;
    static Stack<Integer> stack;
    static List<Set<Integer>> result;
    static int tmp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int test_case = 1; test_case <= T; test_case++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int V = Integer.parseInt(st.nextToken());
            int E = Integer.parseInt(st.nextToken());
            visited = new int[V + 1];
            onStack = new boolean[V + 1];
            stack = new Stack<>();
            graph = new ArrayList[V + 1];
            cost = new int[V + 1][V + 1];
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

            int res = Integer.MAX_VALUE;
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
            if (res == Integer.MAX_VALUE) {
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