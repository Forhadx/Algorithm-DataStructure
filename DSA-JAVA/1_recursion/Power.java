public class Power {
    public static void main(String[] args) {
        int p = pow(2, 3);
        System.out.println(p);  // 8 = 2 * 2 * 2
    }   
    
    public static int pow(int x, int n) {
        if(n == 0) return 1;
        return x * pow(x, n-1);
    }
}
