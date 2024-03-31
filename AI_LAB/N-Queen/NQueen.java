import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class NQueen {
    private int N;
    private List<int[][]> solutions;

    public NQueen(int N) {
        this.N = N;
        this.solutions = new ArrayList<>();
    }

    private void printSolution(int[][] board) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(" " + board[i][j] + " ");
            }
            System.out.println();
        }
    }

    private boolean isSafe(int[][] board, int row, int col) {
        int i, j;

        for (i = 0; i < col; i++) {
            if (board[row][i] == 1) {
                return false;
            }
        }

        for (i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 1) {
                return false;
            }
        }

        for (i = row, j = col; j >= 0 && i < N; i++, j--) {
            if (board[i][j] == 1) {
                return false;
            }
        }

        return true;
    }

    private boolean solveNQUtil(int[][] board, int col) {
        if (col >= N) {
            int[][] solution = new int[N][N];
            for (int i = 0; i < N; i++) {
                System.arraycopy(board[i], 0, solution[i], 0, N);
            }
            solutions.add(solution);
            return true;
        }

        boolean res = false;
        for (int i = 0; i < N; i++) {
            if (isSafe(board, i, col)) {
                board[i][col] = 1;
                res = solveNQUtil(board, col + 1) || res;
                board[i][col] = 0; // BACKTRACK
            }
        }

        return res;
    }

    public List<int[][]> solveNQ() {
        int[][] board = new int[N][N];
        solveNQUtil(board, 0);
        return solutions;
    }

    public static void main(String[] args) {
        // int n = 4;
        int n;
        Scanner sc = new Scanner(System.in);
        System.out.println("Number of queens to place: ");
        n = sc.nextInt();
        NQueen queen = new NQueen(n);
        List<int[][]> solutions = queen.solveNQ();
        int idx = 1;
        for (int[][] solution : solutions) {
            System.out.println("Solution " + idx + ":");
            queen.printSolution(solution);
            System.out.println();
            idx++;
        }
    }
}
