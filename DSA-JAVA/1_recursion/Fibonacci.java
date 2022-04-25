public class Fibonacci {
    public static void main(String[] args) {
        int f = fib(7 );
        System.out.println(f); // 13 , sum of fibonacci numbers
    }       
    
    public static int fib(int n) {
        if(n <= 1 || n<=0) return n;
        return fib(n-1) + fib(n-2);        
    }
}
