
class BinaryTree{
    String[] arr;
    int lastUsedIndex;

    public BinaryTree(int size){
        arr = new String[size+1];
        this.lastUsedIndex = 0;
        System.out.println("Binary tree size: "+size);
    }

    //isFull
    boolean isFull(){
        if(arr.length-1 == lastUsedIndex){
            return true;
        }else{
            return false;
        }
    }

    //insert method
    void insert(String value){
        if(!isFull()){
            arr[lastUsedIndex+1] = value;
            lastUsedIndex++;
            System.out.println("insert value: "+value);
        }else{
            System.out.println("Binary tree is full.");
        }
    }

    // Preorder traversal
    public void preOrder(int index){
        if(index > lastUsedIndex){
            return;
        }
        System.out.print(arr[index]+" ");
        preOrder(index * 2);
        preOrder(index * 2 + 1);
    }

    // Inorder traversal
    public void inOrder(int index){
        if(index > lastUsedIndex){
            return;
        }
        inOrder(index * 2);
        System.out.print(arr[index]+" ");
        inOrder(index * 2 + 1);
    }

    // Postorder traversal
    public void postOrder(int index){
        if(index > lastUsedIndex){
            return;
        }
        postOrder(index * 2);
        postOrder(index * 2 + 1);
        System.out.print(arr[index]+" ");
    }

    // level order traversal
    public void levelOrder(){
        for(int i=1; i<lastUsedIndex; i++){
            System.out.print(arr[i]+" ");
        }
    }

    // search method
    public int searchBT(String value){
        for(int i=1; i<=lastUsedIndex; i++){
            if(arr[i] == value){
                System.out.println(value+ " exist at: "+i);
                return i;
            }
        }
        System.out.println(value+ " not exists in BT.");
        return -1;
    }

    //delete method
    public void delete(String value){
        int location = searchBT(value);

        if(location== -1){
            return;
        }
        arr[location] = arr[lastUsedIndex];
        lastUsedIndex--;
        System.out.println("The node successfully deleted.");
    }

    // delete Bt
    public void deleteBt(){
        arr = null;
        System.out.println("The BT deleted successfully.");
    }
}


public class BT_array {
    public static void main(String[] args) {
        BinaryTree Bt = new BinaryTree(9);

         Bt.insert("N1");
         Bt.insert("N2");
         Bt.insert("N3");
         Bt.insert("N4");
         Bt.insert("N5");
         Bt.insert("N6");
         Bt.insert("N7");
         Bt.insert("N8");
         Bt.insert("N9");
         System.out.println("---------------------");

         System.out.println("Preorder: ");
         Bt.preOrder(1);
         System.out.println();

         System.out.println("Inorder: ");
         Bt.inOrder(1);
         System.out.println();

         System.out.println("Postorder: ");
         Bt.postOrder(1);
         System.out.println();

         System.out.println("Levelorder: ");
         Bt.levelOrder();
         System.out.println();

         Bt.searchBT("N5");

         Bt.delete("N5");
         Bt.levelOrder();

         Bt.deleteBt();

    }
}
