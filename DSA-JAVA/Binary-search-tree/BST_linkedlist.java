import java.util.LinkedList;
import java.util.Queue;

import javax.naming.directory.SearchControls;

class BinaryNode {
    public int value;
    public int height;
    public BinaryNode left;
    public BinaryNode right;
}

class BinarySearchTree{
    BinaryNode root;

    BinarySearchTree(){
        root = null;
    }

    // insert 
    private BinaryNode insert(BinaryNode currentNode, int value){
        if(currentNode == null){
            BinaryNode newNode = new BinaryNode();
            newNode.value = value;
            System.out.println(value+" - inserted");
            return newNode;
        }else if(value <= currentNode.value){
            currentNode.left = insert(currentNode.left, value);
            return currentNode;
        }else{
            currentNode.right = insert(currentNode.right, value);
            return currentNode;
        }
    }

    void insert(int value){
       root =  insert(root, value);
    }

    // preorder traversal
    public void preOrder(BinaryNode node){
        if(node == null){
            return;
        }
        System.out.print(node.value+" ");
        preOrder(node.left);
        preOrder(node.right);
    }

    // Inorder traversal
    public void inOrder(BinaryNode node){
        if(node == null){
            return;
        }
        inOrder(node.left);
        System.out.print(node.value+" ");
        inOrder(node.right);
    }

    // Postorder traversal
    public void postOrder(BinaryNode node){
        if(node == null){
            return;
        }
        postOrder(node.left);
        postOrder(node.right);
        System.out.print(node.value+" ");
    }

    //levelorder traversal
    public void levelorder(){
        Queue<BinaryNode> queue = new LinkedList<BinaryNode>();
        queue.add(root);
        while(!queue.isEmpty()){
            BinaryNode presentNode = queue.remove();
            System.out.print(presentNode.value+" ");
            if(presentNode.left != null){
                queue.add(presentNode.left);
            }
            if(presentNode.right != null){
                queue.add(presentNode.right);
            }
        }
    }

    // search
    public BinaryNode search(BinaryNode node, int value){
        if(node == null){
            System.out.println(value+" not found in BST.");
            return null;
        }else if(node.value == value){
            System.out.println(value+" found in BST.");
            return node;
        }else if(node.value > value){
            return search(node.left, value);
        }else{
            return search(node.right, value);
        }
    }

    // minimum node (successor)
    public static BinaryNode minimumNode(BinaryNode root){
        if(root.left == null){
            return root;
        }else{
            return minimumNode(root.left);   
        }
    }

    // Delete node
    public BinaryNode deleteNode(BinaryNode root, int value){
        if(root == null){
            System.out.println("value not found in BST.");
            return null;
        }
        if(value < root.value){
            root.left = deleteNode(root.left, value);
        }else if(value > root.value){
            root.right = deleteNode(root.right, value);
        }else{
            if(root.left != null && root.right != null){
                BinaryNode temp = root;
                BinaryNode minNodeForRight = minimumNode(temp.right);
                root.value = minNodeForRight.value;
                root.right = deleteNode(root.right, minNodeForRight.value);
            }else if(root.left != null){
                root = root.left;
            }else if(root.right != null){
                root = root.right;
            }else{
                root = null;
            }
        }

        return root;
    }

    // delete BST
    public void  deleteBST(){
        root = null;
        System.out.println("BST deleted");
    }
}


public class BST_linkedlist {
    public static void main(String[] args) {
        BinarySearchTree BST = new BinarySearchTree();
        
        BST.insert(70);
        BST.insert(50);
        BST.insert(90);
        BST.insert(30);
        BST.insert(60);
        BST.insert(80);
        BST.insert(100);
        BST.insert(20);
        BST.insert(40);

        System.out.println("Preorder:");
        BST.preOrder(BST.root);
        System.out.println();

        System.out.println("Inorder: ");
        BST.inOrder(BST.root);
        System.out.println();
       
        System.out.println("Postorder: ");
        BST.postOrder(BST.root);
        System.out.println();
        
        System.out.println("Levelorder: ");
        BST.levelorder();
        System.out.println();

        BST.search(BST.root, 40);

        BST.deleteNode(BST.root, 50);
        BST.levelorder();
        System.out.println();

        BST.deleteBST();

    }    
}
