import java.io.*;
import java.util.*;

public class Main {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int k = 0;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if ((j == 0 && (i % 2) == 1) || (j == n && (i % 2) == 0)) {
          System.out.print("S ");
        } else {
          System.out.print("  ");
        }
      }
      System.out.println();
    }
  }
}
