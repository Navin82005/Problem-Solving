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

  void insertSequenceElementsAfterOddValueNodes(int[] sequence) {
    int n = sequence.length;

    if (head == null) {
      for (int i = n - 1; i >= 0; i--) {
        Node newNode = new Node(sequence[i]);
        newNode.next = head;
        head = newNode;
      }
      return;
    }

    Node temp = head; // using temporary variable for traversing the linked list.
    int k = 0;
    while (temp.next != null && k < n) {
      if (temp.val % 2 == 1) {
        Node newNode = new Node(sequence[k++]);
        newNode.next = temp.next;
        temp.next = newNode;
        temp = temp.next;
      }
      temp = temp.next;
    }
    if (k < n) {
      while (temp.next != null) {
        temp = temp.next;
      }
      while (k < n) {
        Node newNode = new Node(sequence[k++]);
        temp.next = newNode;
        temp = temp.next;
      }
    }
  }

  void display() {
    Node temp = head; // creating temp variable for traversal.

    while (temp != null) { // checking if the temp reaches the end of the linked list.
      System.out.println(temp.val); // printing the value of the current node.
      temp = temp.next; // then moving the pointer to the next.
    }
  }
}

public class AddElementsAfterOddValuesInALinkedList {

  public static void main(String[] args) {
    LinkedList list = new LinkedList();
    list.append(1);
    list.append(2);
    list.append(3);
    list.append(4);
    int[] a = { 6, 9 };
    list.insertSequenceElementsAfterOddValueNodes(a);
    list.display();
  }
}
