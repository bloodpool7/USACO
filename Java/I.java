import java.util.Scanner;
import java.util.Arrays;
public class I {
    public static void main(String[] args){
        Scanner kb = new Scanner(System.in);
        int n, m;
        n = kb.nextInt();
        m = kb.nextInt();

        int[] nums = new int[n];
        for (int i = 0; i < n; i++){
            nums[i] = kb.nextInt();
        }

        int[][] ranges = new int[m][2];
        for (int i = 0; i < m; i++){
            ranges[i][0] = kb.nextInt() - 1;
            ranges[i][1] = kb.nextInt() - 1;
        }

        for (int i = 0; i < m; i++){
            int min = nums[ranges[i][0]];
            for (int j = ranges[i][0]; j <= ranges[i][1]; j++){
                if (nums[j] < min)
                    min = nums[j];
            }
            System.out.println(min);
        }
    }
}
