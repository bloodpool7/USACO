import java.util.Scanner;
public class HungryCow {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        long n = reader.nextLong();
        long t = reader.nextLong();
        long sum = 0;
        long day = 0;
        for (int i =0; i < n; i++){
            long thisday = reader.nextLong();
            day = Math.max(thisday, day);
            long bales = reader.nextLong();
            if (day + bales > t){
                sum += t - day + 1;
                break;
            }
            else {
                sum += bales;
                day += bales;
            }
        }
        System.out.println(sum);
    }
}
