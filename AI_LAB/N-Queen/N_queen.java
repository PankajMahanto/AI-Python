import java.util.Scanner;

public class N_queen {

    int N;

    N_queen(int a) {
        N = a;
    }

    void printSolution(int board[][]) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(" " + board[i][j] + " ");
            }
            System.out.println();
        }
    }

    boolean isSafe(int grid[][], int row, int col) {
        int i, j;

        for (i = 0; i < col; i++) {
            if (grid[row][i] == 1) {
                return false;
            }
        }

        for (i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (grid[i][j] == 1) {
                return false;
            }
        }

        for (i = row, j = col; j >= 0 && i < N; i++, j--) {
            if (grid[i][j] == 1) {
                return false;
            }
        }

        return true;
    }

    boolean solveNQUtil(int grid[][], int col) {
        if (col >= N) {
            return true;
        }

        for (int i = 0; i < N; i++) {
            if (isSafe(grid, i, col)) {
                grid[i][col] = 1;
                if (solveNQUtil(grid, col + 1)) {
                    return true;
                }
                grid[i][col] = 0; // BACKTRACK
            }
        }

        return false;
    }

    boolean solveNQ() {
        int grid[][] = new int[N][N];
        if (!solveNQUtil(grid, 0)) {
            System.out.print("Solution does not exist for " + N + " queens");
            return false;
        }
        System.out.println("Solution found for " + N + " queens");
        printSolution(grid);
        return true;
    }

    public static void main(String args[]) {
        int n;
        Scanner sc = new Scanner(System.in);
        System.out.println("Number of queens to place: ");
        n = sc.nextInt();
        N_queen Queen = new N_queen(n);
        Queen.solveNQ();
    }
}
