public class GCD {
    public static void main(String[] args) {
        System.out.println(gcd(10, 4)); // 2
        System.out.println(gcd(4, 12)); // 4
        System.out.println(gcd(-8, 12)); // -1
    }

    public static int gcd(int a, int b) {
        if(a<0 || b<0) return -1;
        
        if(b == 0) return a;

        return gcd(b, a%b);
    }
}
