class Node {

  int val; // val or data
  Node next; // pointer to point the next node.

  Node(int value) { // Constructor for initializing value
    val = value;
    next = null;
  }
}

class LinkedList {

  Node head; // linked list's head.

  void append(int data) { // function to add data to the linked list.
    Node newNode = new Node(data); // creating a new node of the given data
    if (head == null) { // checking if the linked list is empty.
      head = newNode; // assigning the new node directly to head.
      return; // stopping further execution in the function by using return.
    }

    Node temp = head; // using temporary variable for traversing the linked list.
    while (temp.next != null) { // running while loop until the temp reaches the end node.
      temp = temp.next; // moving the temp variable to the next node of the linked list.
    }
    temp.next = newNode; // adding the new node after the last node.
  }

  void insertInPosition(int pos, int val) {
    Node newNode = new Node(val);

    if (head == null) {
      head = newNode;
      return;
    }

    Node temp = head; // using temporary variable for traversing the linked list.
    pos--;
    while (temp.next != null && pos != 1) { // checking if the temp end, and for the pos variable to reach the target node
      pos--; // reducing the pos variable so to reach the target node's position.
      temp = temp.next; // moving the temp pointer.
    }
    newNode.next = temp.next; // assigning the rest of the linked list after the target node to the new node's right.
    temp.next = newNode; // assigning the target node's next to the new node along with the rest of the nodes.
  }

  void display() {
    Node temp = head; // creating temp variable for traversal.

    while (temp != null) { // checking if the temp reaches the end of the linked list.
      System.out.println(temp.val); // printing the value of the current node.
      temp = temp.next; // then moving the pointer to the next.
    }
  }
}

class Custom {

  public static void main(String[] args) {
    LinkedList list = new LinkedList();
    list.append(1);
    list.append(2);
    list.append(4);
    list.append(5);
    list.insertInPosition(3, 3);
    list.display();
  }
}
