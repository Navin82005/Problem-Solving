import java.util.Scanner;

class GridPropagation {

  static boolean isValidTileToExplode(int[][] a, int i, int j) {
    int n = a.length;
    int m = a[0].length;
    return ((0 <= i && i < n) && (0 <= j && j < m));
  }

  static void explodeTheAdjacent(int[][] a, int i, int j) {
    int[] dx = { -1, 1, 0, 0, 1, -1, 1, -1 };
    int[] dy = { 0, 0, 1, -1, 1, -1, -1, 1 };

    for (int k = 0; k < 8; k++) {
      int newI = i + dx[k];
      int newJ = j + dy[k];
      if (isValidTileToExplode(a, newI, newJ)) {
        if (a[newI][newJ] == 1) {
          a[newI][newJ] = 0;
        }
        if (a[newI][newJ] == 9) {
          a[newI][newJ] = 1;
        }
      }
    }
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt(), m = sc.nextInt();
    int[][] a = new int[n][m];

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        a[i][j] = sc.nextInt();
      }
      sc.nextLine();
    }

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (a[i][j] == 2) {
          explodeTheAdjacent(a, i, j);
        }
      }
    }
    System.out.println();
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        System.out.print(a[i][j] + " ");
      }
      System.out.println();
    }

    sc.close();
  }
}
