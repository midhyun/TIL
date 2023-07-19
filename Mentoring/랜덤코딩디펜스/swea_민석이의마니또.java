public class Main {
    static int id = 0;

    static int dfs(cur) {
        id++;
        System.outprintln(id);
    }

    public static void main(String[] args) {
        dfs(1);
    }
}