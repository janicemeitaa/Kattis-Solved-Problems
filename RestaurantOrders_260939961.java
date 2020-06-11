import java.util.*;

public class RestaurantOrders {
	
	public static void main(String[] args) {
	    
		Scanner sc = new Scanner(System.in);
		int n, m;
		int[] costs;
		int[] costOfOrder;
		int[] orderNum;
		
	    n = sc.nextInt();
		costs = new int[n];
		for(int i = 0; i<n; i++) {
			costs[i] = sc.nextInt();
		}
		
		m = sc.nextInt();
		costOfOrder = new int[m];
		for(int i = 0; i<m; i++) {
			costOfOrder[i] = sc.nextInt();
		}
		sc.close();
		
		orderNum = new int[30001];
		Arrays.fill(orderNum,  -1);
		orderNum[0]=1;
		for (int i=0; i<costs.length; i++) {
			for (int j=costs[i]; j<orderNum.length; j++) {
				if (orderNum[j-costs[i]]==-1) {
				    continue;
				}
				if (orderNum[j]==-1) {
				    orderNum[j] = orderNum[j-costs[i]];
				} else {
				    orderNum[j] = orderNum[j-costs[i]] + 1;
				}
			}
		}
		
		for (int c=0; c<costOfOrder.length; c++) {
			if (orderNum[costOfOrder[c]]<1) {
			    System.out.println("Impossible");
			} else if (orderNum[costOfOrder[c]]>1) {
			    System.out.println("Ambiguous");
			} else {
				for (int i=0; i<costs.length; i++) {
					while (costOfOrder[c]>=costs[i] && orderNum[costOfOrder[c]-costs[i]]==1) {
						costOfOrder[c] = costOfOrder[c]-costs[i];
						System.out.print(i+1 + " ");
					}
				}
				System.out.println();
			}
		}
	}
}