import java.util.*;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String s = sc.nextLine();
    String a = sc.nextLine();

    // Getting lengths of each strings
    int n = s.length();
    int m = a.length();
    int i = 0, j = 0; // pointer to traverse both the strings

    while (i < n && j < m) {
      if (s.charAt(i) == a.charAt(j)) { // Checking if both the characters are equal
        i++; // Incrementing the i pointer, so can check the next character form string s
      }
      j++; // Incrementing the j pointer, so can check the next character form string a
    }
    sc.close();

    if (i == n) {
      System.out.println("True");
    } else {
      System.out.println("False");
    }
  }
}
