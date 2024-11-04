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
        System.out.println(Trie.sb.toString());
    }
}

class TrieNode implements Comparable<TrieNode> {
    TreeSet<TrieNode> children; // 자식 노드를 저장하는 맵
    String value; // 현재 노드의 값;
    boolean isEndOfWord;

    //생성자
    public TrieNode() {
        children = new TreeSet<>();
        isEndOfWord = false;
    }

    public TrieNode(String value) {
        this();
        this.value = value;
    }

    // compareTo 메소드 구현
    @Override
    public int compareTo(TrieNode o) {
        return value.compareTo(o.value);
    }
}

class Trie {
    static StringBuilder sb = new StringBuilder();
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
            TrieNode finalCurrentNode = currentNode;
            currentNode = currentNode.children.stream()
                    .filter(node -> node.value.equals(dir))
                    .findFirst()
                    .orElseGet(() -> {
                        TrieNode newNode = new TrieNode(dir);
                        finalCurrentNode.children.add(newNode);
                        return newNode;
                    });
        }
        currentNode.isEndOfWord = true;
    }

    public void printAllPath(int depth, TrieNode node) {
        for (TrieNode child : node.children) {
            String value = child.value;
            sb.append(" ".repeat(Math.max(0, depth)));
            sb.append(value).append("\n");

            printAllPath(depth + 1, child);
        }
    }

}