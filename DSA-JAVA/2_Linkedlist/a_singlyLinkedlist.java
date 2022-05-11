class Node {
    public int value;
    public Node next;
}



class Singlylist{
    public Node head;
    public Node tail;
    public int size;

    public Node createSingleLinkedlist(int nodeValue){
        // head = new Node();
        Node node = new Node();
        node.value = nodeValue;
        node.next = null;
        head = node;
        tail = node;
        size = 1;
        return head;
    }


    // INSERT
    public void insertInLinkedList(int nodeValue, int location){
        Node node = new Node();
        node.value = nodeValue;

        if(head == null){
            createSingleLinkedlist(nodeValue);
            return;
        }else if(location == 0){
            node.next = head;
            head = node;
        }else if(location >= size){
            node.next = null;
            tail.next = node;
            tail = node;
        }else{
            Node tempNode = head;
            int index = 0;
            while(index < location - 1){
                tempNode = tempNode.next;
                index++;
            }
            Node nextNode = tempNode.next;
            tempNode.next = node;
            node.next =  nextNode;
        }
        size++;
    }


    // Traverse list
    public void traverseSinglylist(){
        if(head == null){
            System.out.println("Sll doesn't exist!");
        }else{
            Node tempNode = head;
            for(int i=0; i<size; i++){
                System.out.print(tempNode.value);
                if(i != size-1){
                    System.out.print(" -> ");
                }
                tempNode = tempNode.next;
            }
            System.out.println("\n");
        }
    }


    // Search for a node
    boolean searchNode(int nodeValue){
        if(head != null){
            Node tempNode = head;

            for(int i=0; i<size; i++){
                if(tempNode.value == nodeValue){
                    System.out.println("Found the node at location: "+i+"\n");
                    return true;
                }
                tempNode = tempNode.next;
            }
        }

        System.out.println("Node not found");
        return false;
    }


    // delete node
    public void deleteofNode(int location){
        if(head == null){
            System.out.println("The SLL doesn't exist!");
            return;
        }else if(location == 0){
            head = head.next;
            size--;
            if(size == 0){
                tail = null;
            }
        }else if(location >= size){
            Node tempNode = head;
            for(int i=0; i<size-1; i++){
                tempNode = tempNode.next;
            }
            if(tempNode == head){
                tail = head =  null;
                size--;
                return;
            }
            tempNode.next = null;
            tail = tempNode;
            size--;
        }else{
            Node tempNode = head;
            for(int i=0; i<location-1; i++){
                tempNode = tempNode.next;
            }
            tempNode.next = tempNode.next.next;
            size--;
        }
    }

    // delete entire list
    public void deleteSll(){
        head = null;
        tail = null;
        System.out.println("The sll deleted successfully!");
    }
}


class a_singlyLinkedlist{
    public static void main(String[] args) {

        Singlylist  sll = new Singlylist();

        sll.createSingleLinkedlist(5);
        // System.out.println(sll.head.value);
        
        sll.insertInLinkedList(6,1);
        sll.insertInLinkedList(88,1);
        sll.insertInLinkedList(7,3);
        sll.insertInLinkedList(8,4);
        sll.insertInLinkedList(9,5);

        sll.traverseSinglylist();

        sll.searchNode(6);

        sll.deleteofNode(32);
        sll.traverseSinglylist();
        sll.deleteSll();

    }
}