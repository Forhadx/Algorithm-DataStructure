class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
    this.prev = null;
  }
}

class LinkList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  insertLast(value) {
    console.log("INSERT LAST: ", value);
    let newNode = new Node(value);

    if (this.head === null) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      newNode.prev = this.tail;
      this.tail = newNode;
    }
    this.size++;
  }

  insertFirst(value) {
    console.log("INSERT FIRST: ", value);
    let newNode = new Node(value);

    if (this.head === null) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      newNode.next = this.head;
      this.head.prev = newNode;
      this.head = newNode;
    }
    this.size++;
  }

  insertByLoc(value, loc) {
    let newNode = new Node(value);

    // Invalid loc
    if (loc < 0 || this.size + 1 < loc) {
      console.log("Invalid location!");
      return;
    }

    // no data exist
    if (this.head === null) {
      this.head = newNode;
      this.tail = newNode;
    }
    // insert first
    else if (loc === 1) {
      console.log(`INSERT AT FIRST(${loc}): `, value);
      this.head.prev = newNode;
      newNode.next = this.head;
      this.head = newNode;
    }
    // insert last
    else if (loc === this.size + 1) {
      console.log(`INSERT AT LAST(${loc}): `, value);
      this.tail.next = newNode;
      newNode.prev = this.tail;
      this.tail = newNode;
    }
    // insert middle any loc
    else {
      console.log(`INSERT AT ${loc}: `, value);
      let tempHead = this.head;
      let i = 1;
      while (tempHead.next !== null) {
        if (i === loc) {
          newNode.prev = tempHead.prev;
          newNode.next = tempHead;
          tempHead.prev.next = newNode;
          tempHead.prev = newNode;
          break;
        }
        tempHead = tempHead.next;
        i++;
      }
    }
    this.size++;
  }

  deleteByLoc(loc) {
    // Invalid loc
    if (loc < 0 || this.size + 1 < loc || this.head === null) {
      console.log("Invalid location!");
      return;
    }

    // delete first
    if (loc === 1) {
      console.log(`DELETE AT FIRST(${loc})`);
      this.head = this.head.next;
      this.head.prev = null;
    }
    // delete last
    else if (loc === this.size) {
      console.log(`DELETE AT LAST(${loc})`);
      this.tail = this.tail.prev;
      this.tail.next = null;
    }
    // delete middle any loc
    else {
      console.log(`DELETE AT ${loc}`);
      let tempHead = this.head;
      let i = 1;
      while (tempHead.next !== null) {
        if (i === loc) {
          tempHead.prev.next = tempHead.next;
          tempHead.next.prev = tempHead.prev.next;
          break;
        }
        tempHead = tempHead.next;
        i++;
      }
    }
    this.size--;
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
    if (this.head !== null) {
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

lList.insertLast(1);
lList.insertLast(5);
lList.insertLast(9);
lList.insertFirst(8);
lList.traverse();

lList.insertByLoc(22, 1);

lList.insertByLoc(23, 6);
lList.insertByLoc(55, 3);
lList.traverse();
lList.manualSize();

lList.deleteByLoc(7);
lList.traverse();
lList.deleteByLoc(1);
lList.traverse();
lList.deleteByLoc(3);
lList.traverse();

// console.log(lList);
