import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int test = sc.nextInt();
        int result[] = new int[test];

        for(int i = 0; i<test;i++){
            int start = sc.nextInt();
            int end = sc.nextInt();
            int distance = end - start;
            int max = (int)Math.sqrt(distance);

            if(max == Math.sqrt(distance)) {
                result[i]= (max * 2 - 1);
            }
            else if(distance <= max * max + max) {
                result[i] = max*2;
            }
            else {
                result[i] = max*2+1;
            }


        }

        for(int i = 0; i<test;i++){
            System.out.println(result[i]);
        }

    }
}
