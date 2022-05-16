public class BinarySearch {
    public static void main(String[] args) {
        int[] arr = {12, 15, 23, 24, 35, 46, 75, 98};
        int val = 40;

        int start = 0; 
        int end = arr.length - 1;
        
        while(start<=end){
            int middle = (start+end)/2;

            if(arr[middle] == val){
                System.out.println(val+" found at: "+middle);
                break;
            }else if(arr[middle] > val){
                end = middle - 1;
            }else{
                start = middle + 1;
            }
        }

    }
}
