public class LinearSearch {
    public static void main(String[] args) {
        int[] arr = {3, 2, 1, 6, 4, 5};
        int val = 6;

        for(int i=0; i<arr.length; i++){
            if(arr[i] == val){
                System.out.println(val+" found at: "+i);
                break;
            }
        }
    }
}
