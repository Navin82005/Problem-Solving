package patterns;

import java.util.Scanner;

/*
 * input = 3
 * output:
 *     1 A
 *   3 1 A C
 * 5 3 1 A C E
 */

public class Pattern {

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int n = sc.nextInt();

    int k = 0, l = 1;
    for (int i = 1; i <= n; i++) {
      for (int j = i; j < n; j++) {
        System.out.print("  ");
      }
      k = 2 * i - 1;
      for (int j = 0; j < i; j++) {
        System.out.print(k + " ");
        k -= 2;
      }
      char c = 'A';
      for (int j = 0; j < i; j++) {
        System.out.print(c + " ");
        c += 2;
      }
      System.out.println();
    }
    sc.close();
  }
}
