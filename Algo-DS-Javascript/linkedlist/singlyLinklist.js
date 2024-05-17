class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class LinkList {
  constructor() {
    this.head = null;
    this.size = 0;
  }

  insertFirst(value) {
    let newNode = new Node(value);
    newNode.next = this.head;
    this.head = newNode;
    this.size++;
  }

  insertLast(value) {
    let newNode = new Node(value);
    if (this.head === null) {
      this.head = newNode;
      this.size++;
    } else {
      let tempHead = this.head;
      while (tempHead.next !== null) {
        tempHead = tempHead.next;
      }
      tempHead.next = newNode;
      this.size++;
    }
  }

  insertByLoc(value, loc) {
    // Invalid loc
    if (loc < 0 || this.size < loc) {
      console.log("Invalid location!");
    }

    // insert first
    else if (loc === 0) {
      let newNode = new Node(value);
      newNode.next = this.head;
      this.head = newNode;
      this.size++;
    }
    
    // insert any loc
    else {
      let newNode = new Node(value);
      let tempHead = this.head;
      let i = 0;
      while (tempHead !== null) {
        if (i === loc - 1) {
          newNode.next = tempHead.next;
          tempHead.next = newNode;
        }
        tempHead = tempHead.next;
        i++;
      }
      this.size++;
    }
  }

  deleteByLoc(loc) {
    // Invalid loc
    if (loc < 0 || this.size < loc) {
      console.log("Invalid location!");
    }

    // delete first
    else if (loc === 0) {
      let tempHead = this.head;
      this.head = tempHead.next;
      this.size--;
    }

    // insert any loc
    else {
      let tempHead = this.head;
      let i = 0;
      while (tempHead !== null) {
        if (i === loc - 2) {
          tempHead.next = tempHead.next.next;
          break;
        }
        tempHead = tempHead.next;
        i++;
      }
    }
  }

  traverse() {
    let listStr = "";
    if (this.head === null) {
      console.log("No data to insert!");
    } else {
      let tempHead = this.head;
      while (tempHead !== null) {
        listStr += tempHead.data + (tempHead.next ? " -> " : "");
        tempHead = tempHead.next;
      }
      console.log("Traverse: ", listStr);
    }
  }

  manualSize() {
    let tempSize = 0;
    if (this.head === null) {
      tempSize++;
    } else {
      let tempHead = this.head;
      while (tempHead !== null) {
        tempHead = tempHead.next;
        tempSize++;
      }
    }
    console.log("List size: ", tempSize);
  }
}

let lList = new LinkList();

lList.insertFirst(9);
lList.insertFirst(2);
lList.insertFirst(4);

lList.insertLast(19);
lList.insertLast(33);

lList.insertByLoc(57, 3);

lList.traverse();

console.log("After delete");
lList.deleteByLoc(6);
lList.traverse();

lList.manualSize();
