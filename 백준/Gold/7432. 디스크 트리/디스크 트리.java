import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Trie trie = new Trie();

        for (int i = 0; i < N; i++) {
            String[] path = br.readLine().split("\\\\");
            trie.insert(path);
        }
        TrieNode root = trie.getRoot();
        trie.printAllPath(0, root);
        System.out.println(trie.sb.toString());
    }
}

class TrieNode {
    Map<String, TrieNode> children; // 자식 노드를 저장하는 맵
    boolean isEndOfWord;

    //생성자
    public TrieNode() {
        children = new HashMap<>();
        isEndOfWord = false;
    }
}

class Trie {
    StringBuilder sb = new StringBuilder();
    private final TrieNode root;
    // 생성자: 루트노드를 초기화
    public Trie() {
        root = new TrieNode();
    }

    public TrieNode getRoot() {
        return this.root;
    }

    public void insert(String[] path) {
        TrieNode currentNode = root;
        for (String dir : path) {
            currentNode = currentNode.children.computeIfAbsent(dir, k -> new TrieNode());
        }
        currentNode.isEndOfWord = true;
    }

    public void printAllPath(int depth, TrieNode node) {
        List<String> children = new ArrayList<>(node.children.keySet());

        Collections.sort(children);
        for (String key : children) {
            TrieNode child = node.children.get(key);
            for (int i = 0; i < depth; i++) {
                sb.append(" ");
            }
            sb.append(key).append("\n");
            printAllPath(depth + 1, child);
        }
    }

}