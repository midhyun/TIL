import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;

public class TarjanAlgorithm {
    static int id = 0;
    static List<Integer>[] graph;
    static int[] visited;
    static boolean[] onStack;
    static Stack<Integer> stack;
    static List<List<Integer>> result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());
        visited = new int[V + 1];
        onStack = new boolean[V + 1];
        stack = new Stack<>();
        graph = new ArrayList[V + 1];
        for (int i = 1; i <= V; i++) {
            graph[i] = new ArrayList<>();
        }
        result = new ArrayList<>();

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
        }

        for (int i = 1; i <= V; i++) {
            if (visited[i] == 0) {
                dfs(i);
            }
        }

        System.out.println(result.size());
        result.sort((a, b) -> a.get(0).compareTo(b.get(0)));
        for (List<Integer> list : result) {
            for (int num : list) {
                System.out.print(num + " ");
            }
            System.out.println();
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
            List<Integer> css = new ArrayList<>();
            while (true) {
                int x = stack.pop();
                onStack[x] = false;
                css.add(x);
                if (x == cur) {
                    break;
                }
            }
            css.sort(null);
            css.add(-1);
            result.add(css);
        }

        return parent;
    }
}
