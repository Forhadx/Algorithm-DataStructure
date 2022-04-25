public class sumOfDigit {
    public static void main(String[] args) {
        int x = sum(5113);
        System.out.println(x);  // 5+1+1+3 = 10
    }   
    
    public static int sum(int n) {
        if(n == 0) return 0;
        return (n%10) + sum(n/10);
    }
}
