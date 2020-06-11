import java.util.Arrays;
import java.util.Scanner;

public class ColoringSocks {
    public static void main(String[] args) {
        int[] socks;
        int S, C, K;
        Scanner sc = new Scanner(System.in);

        S = sc.nextInt();
        C = sc.nextInt();
        K = sc.nextInt();
        socks = new int[S];

        for (int i = 0; i < S; i++) {
            socks[i] = sc.nextInt();
        }

        Arrays.sort(socks);

        int machineCount = 0;
        int idx = 0;

        for (int j = 0; j < S; j++) {
            if (j == S - 1) {
                machineCount++;
                break;
            }
            if (socks[j + 1] - socks[idx] > K || j - idx == C - 1) {
                machineCount++;
                idx = j + 1;
            }
        }

        System.out.println(machineCount);

    }
}