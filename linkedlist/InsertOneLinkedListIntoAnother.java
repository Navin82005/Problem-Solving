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

  int length() {
    int len = 0;
    Node temp = head;
    while (temp != null) {
      temp = temp.next;
      len++;
    }
    return len;
  }

  void insertLinkedListInAlternatingPositions(Node head2) {
    if (head2 == null) {
      return;
    }

    Node temp = head; // using temporary variable for traversing the linked list.
    Node temp2;
    while (head2 != null) {
      temp2 = head2.next;
      head2.next = temp.next;
      temp.next = head2;
      head2 = temp2;
      temp = temp.next.next;
    }
  }

  void display() {
    Node temp = head; // creating temp variable for traversal.

    while (temp != null) { // checking if the temp reaches the end of the linked list.
      System.out.print(temp.val + " -> "); // printing the value of the current node.
      temp = temp.next; // then moving the pointer to the next.
    }
    System.out.println("null");
  }
}

public class InsertOneLinkedListIntoAnother {

  public static void main(String[] args) {
    LinkedList list1 = new LinkedList();
    LinkedList list2 = new LinkedList();

    list1.append(1);
    list1.append(3);
    list1.append(5);

    list2.append(2);
    list2.append(4);
    list2.append(6);
    list2.append(8);

    list1.display();
    list2.display();

    int n1 = list1.length(), n2 = list2.length();
    if (n1 < n2) {
      list2.insertLinkedListInAlternatingPositions(list1.head);
      list2.display();
    } else {
      list1.insertLinkedListInAlternatingPositions(list2.head);
      list1.display();
    }
  }
}
