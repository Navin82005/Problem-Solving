import java.util.Scanner;

public class MinesweeperCountTheMines {

  static boolean isValidTile(int x, int y, int n) {
    return (0 <= x && x < n) && (0 <= y && y < n);
  }

  static void checkAMine(char[][] a, int x, int y) {
    int n = a.length;

    int[] dx = { -1, 1, 0, 0, 1, -1, 1, -1 };
    int[] dy = { 0, 0, 1, -1, 1, -1, -1, 1 };

    for (int i = 0; i < 8; i++) {
      int nx = x + dx[i];
      int ny = y + dy[i];

      if (isValidTile(nx, ny, n) && a[nx][ny] != '*') {
        a[nx][ny] = (char) (a[nx][ny] + 1);
      }
    }
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    sc.nextLine(); // Consume newline

    char[][] a = new char[n][n];

    for (int i = 0; i < n; i++) {
      String temp = sc.nextLine().replaceAll(" ", "");
      for (int j = 0; j < n; j++) {
        a[i][j] = (temp.charAt(j) == '.') ? '0' : '*';
      }
    }

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        if (a[i][j] == '*') {
          checkAMine(a, i, j);
        }
      }
    }

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        System.out.print(a[i][j] + (j < n - 1 ? " " : ""));
      }
      System.out.println();
    }

    sc.close();
  }
}
