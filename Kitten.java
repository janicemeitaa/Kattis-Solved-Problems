import java.util.Scanner;
import java.util.HashMap;

public class Kitten {
    public static void main(String[] args) {
        HashMap<String, String> tree = new HashMap<>();
        Scanner inp = new Scanner(System.in);
        String pos = inp.nextLine();
        String[] branches;
        String thisRoot;
        
        boolean notEnd = true;
        
        while (notEnd) {
            String line = inp.nextLine();
            if (line.equals("-1")) {
                notEnd = false;
            }
            
            branches = line.split(" ");
            thisRoot = branches[0];
            
            for (int i=1; i<branches.length; i++) {
                tree.put(branches[i], thisRoot);
            }
        }
        
        boolean endOfPath = false;
        String tmp = "";
        
        while (!endOfPath){
            tmp += (pos + " ");

            if (!tree.containsKey(pos)) {
                endOfPath = false;
                break;
            }
            
            pos = tree.get(pos);
        }
        System.out.println(tmp);
    }
}