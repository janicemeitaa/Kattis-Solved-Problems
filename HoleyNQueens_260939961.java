import java.io.BufferedReader;
import java.io.InputStreamReader;

public class HoleyNQueens {
    static int N, M, c;
	static int[] queens;
	static boolean[][] holes;

	public static void main(String[] args) throws Exception {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		while (true) {
			c = 0;
			String[] in = reader.readLine().split(" ");
			N = Integer.parseInt(in[0]);
			M = Integer.parseInt(in[1]);
			if (N == 0 && M == 0) break;
			queens = new int[N + 1];
			holes = new boolean[N + 1][N + 1];
			for (int i = 0; i < N+1; i++) {
				queens[i] = -1;
				for (int j = 0; j < N+1; j++) {
					holes[i][j] = true;
				}
			}
			for (int i = 0; i < M; i++) {
				in = reader.readLine().split(" ");
				int j = Integer.parseInt(in[0]);
				int k = Integer.parseInt(in[1]);
				j++;
				k++;
				holes[j][k] = false;
			}
			possibleSolutions(1);
			System.out.println(c);
		}
	}

	static void possibleSolutions(int row) {
		for (int col = 1; col <= N; col++) {
		    boolean thisTry = true;
		    if (!holes[row][col]) thisTry = false;
		    for (int j = 1; j <= row - 1; j++) {
    			if (queens[j] == col || Math.abs(queens[j] - col) == Math.abs(j - row)) {
    				thisTry = false;
    			}
		    }
			if (thisTry) {
				queens[row] = col;
				if (row == N) {
					c++;
				} else {
					possibleSolutions(row + 1);
				}
			}
		}
	}
}