import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Edge implements Comparable<Edge> {
    int src, dest, weight;

    public Edge(int src, int dest, int weight) {
        this.src = src;
        this.dest = dest;
        this.weight = weight;
    }

    @Override
    public int compareTo(Edge o) {
        return this.weight - o.weight;
    }
}

public class Main {
    int[] parent;
    private List<Edge> edges;

    private int find(int node) {
        if (parent[node] != node) {
            parent[node] = find(parent[node]);
        }
        return parent[node];
    }

    private void union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return;
        if (a < b) {
            parent[b] = a;
        } else {
            parent[a] = b;
        }
    }

    public void KruskalMst(List<Edge> edges, int V) {
        Collections.sort(edges);
        parent = new int[V];

        for (int i = 0; i < V; i++) parent[i] = i;

        int mstWeight = 0;

        for (Edge edge : edges) {
            if (find(edge.src) == find(edge.dest)) continue;
            union(edge.src, edge.dest);
            mstWeight += edge.weight;
        }
        System.out.println(mstWeight);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int test_case = Integer.parseInt(br.readLine());
        for (int i = 0; i<test_case; i++) {
            String[] s = br.readLine().split(" ");
            int R = Integer.parseInt(s[0]);
            int C = Integer.parseInt(s[1]);
            int V = R * C;
            List<Edge> edges = new ArrayList<>();
            for (int j = 0; j < R; j++) {
                String[] s1 = br.readLine().split(" ");
                for (int k = 0; k < C-1; k++) {
                    edges.add(new Edge(j * C + k, j * C + k + 1, Integer.parseInt(s1[k])));
                }
            }
            for (int j = 0; j < R-1; j++) {
                String[] s1 = br.readLine().split(" ");
                for (int k = 0; k < C; k++) {
                    edges.add(new Edge(j * C + k, (j + 1) * C + k, Integer.parseInt(s1[k])));
                }
            }

            Main mst = new Main();
            mst.KruskalMst(edges, V);

        }

    }

}
