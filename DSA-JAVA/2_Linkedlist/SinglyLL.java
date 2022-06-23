

class Node {
	public int value;
	public Node next;
}


class SingleList {
	public Node head;
	public Node tail;
	public int size = 0;

	// insert
	public void intert(int nodeValue) {
		Node node = new Node();
		node.value = nodeValue;
		node.next = null;

		if (head == null)
			head = node;
		else
			tail.next = node;

		tail = node;
		size++;
	}

	// insert by location
	public void insertByLoc(int nodeValue, int loc) {
		Node node = new Node();
		node.value = nodeValue;

		if (head == null) {
			node.next = null;
			head = node;
			tail = node;
		} else if (loc == 0) {
			node.next = head;
			head = node;
		} else if (loc >= size) {
			node.next = null;
			tail.next = node;
			tail = node;
		} else {
			Node temp = head;
			int index = 0;
			while (index < loc - 1) {
				temp = temp.next;
				index++;
			}
			Node nextNode = temp.next;
			temp.next = node;
			node.next = nextNode;
		}

		size++;
	}

	// Delete
	public void delete(int loc) {
		if (head == null) {
			System.out.println("No data");
		} else if (loc == 0) {
			head = head.next;
			size--;
			if (size == 0) {
				tail = null;
			}
		} else if (loc >= size) {
			Node temp = head;
			for (int i = 0; i < size - 1; i++) {
				temp = temp.next;
			}
			if (temp == head) {
				head = tail = null;
				size--;
				return;
			}
			temp.next = null;
			tail = temp;
			size--;
		}else {
			Node temp = head;
			for(int i=0; i<loc-1; i++) {
				temp = temp.next;
			}
			temp.next = temp.next.next;
			size--;
		}
	}

	// Traverse list
	public void travers() {
		if (head == null) {
			System.out.println("No data");
		} else {
			Node temp = head;
			for (int i = 0; i < size; i++) {
				System.out.print(temp.value + " ");
				temp = temp.next;
			}
			System.out.println();
		}
	}
}
public class SinglyLL {

	public static void main(String[] args) {
		SingleList sll = new SingleList();
		sll.intert(10);
		sll.intert(20);
		sll.intert(30);

		sll.insertByLoc(5, 0);
		sll.insertByLoc(40, 2);

		sll.travers();
		
		sll.delete(3);	

		sll.travers();
	}

}
