import java.util.Scanner;

public class Commercials {
	
	public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int p = sc.nextInt();
        int[] breaks = new int[n];
        
        for(int i=0; i<breaks.length; i++) {
            breaks[i] = sc.nextInt()-p;
        }
        
        int idx, max;
        idx = 0;
        max = 0;
        for(int i=0; i<breaks.length; i++){
            idx+=breaks[i];
            if (idx<0) {
                idx=0;
            }
            if (max<idx) {
                max=idx;
            }
        }
        System.out.println(max);
    }
}