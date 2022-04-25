public class decimalToBinary {
    public static void main(String[] args) {
       int bin = decToBin(9);
       System.out.println(bin); // 1001
    }

    public static int decToBin(int n){
        if(n <= 0){
            return 0;
        }
        return (n%2) + decToBin(n/2)*10;
    }
}
