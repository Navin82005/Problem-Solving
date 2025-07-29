import java.util.*;

public class ReverseWordLetters {

  static String revWord(String word) {
    StringBuilder temp = new StringBuilder(word);
    StringBuilder nonDigits = new StringBuilder();

    for (char c : word.toCharArray()) {
      if (!Character.isDigit(c)) {
        if (c >= 'A' && c <= 'Z') {
          nonDigits.append((char) (c + ('a' - 'A')));
        } else {
          nonDigits.append((char) c);
        }
      }
    }
    nonDigits.reverse();

    int index = 0;
    for (int i = 0; i < word.length(); i++) {
      if (!Character.isDigit(word.charAt(i))) {
        temp.setCharAt(i, nonDigits.charAt(index));
        index++;
      }
    }

    return temp.toString();
  }

  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    String a = sc.nextLine();
    String ch[] = a.split(" ");

    StringBuilder res = new StringBuilder();
    for (int i = 0; i < ch.length; i++) {
      String w = ch[i];
      if (!w.matches("[A-Za-z]+[0-9]+[A-Za-z]+")) {
        String rev = new StringBuilder(w).reverse().toString();
        rev = rev.substring(0, 1).toUpperCase() + rev.substring(1);
        // System.out.print(rev+" ");
        res.append(rev).append(" ");
      } else if (w.matches("[0-9]+")) {
        res.append(w).append(" ");
      } else {
        String result = revWord(w);
        res
          .append(result.substring(0, 1).toUpperCase() + result.substring(1))
          .append(" ");
      }
    }
    System.out.print(res.toString().trim());
    sc.close();
  }
}
