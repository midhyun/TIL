import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static int[][] board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        board = new int[9][9];

        for (int i = 0; i < 9; i++) {
            board[i] = br.readLine().chars().map(ch -> ch - '0').toArray();
        }

        sudoku(0, 0);

    }

    private static boolean chk_board(int y, int x) {
        for (int i = 0; i < 9; i++) {
            if (board[y][i] == board[y][x] && i != x) {
                return false;
            }
            if (board[i][x] == board[y][x] && i != y) {
                return false;
            }
        }

        for (int i = (y / 3) * 3; i < (y / 3) * 3 + 3; i++) {
            for (int j = (x / 3) * 3; j < (x / 3) * 3 + 3; j++) {
                if (board[i][j] == board[y][x] && i != y && j != x) {
                    return false;
                }
            }
        }

        return true;
    }

    private static void sudoku(int y, int x) {
        if (y == 9) {
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    System.out.print(board[i][j]);
                }
                System.out.println();
            }
            System.exit(0);
        }

        if (board[y][x] == 0) {
            for (int i = 1; i <= 9; i++) {
                board[y][x] = i;
                if (chk_board(y, x)) {
                    if (x == 8) {
                        sudoku(y + 1, 0);
                    } else {
                        sudoku(y, x + 1);
                    }
                }
                board[y][x] = 0;
            }
        } else {
            if (x == 8) {
                sudoku(y + 1, 0);
            } else {
                sudoku(y, x + 1);
            }
        }
    }
}
