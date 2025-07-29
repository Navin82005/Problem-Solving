package backtracking;

import java.util.Arrays;

class DungeonEscape {

  static void increaseMonsterGaze(int[][] a, int x, int y) {
    int offset = a[x][y] - 1;
    int xStart = x - offset;
    int yStart = y - offset;
    int xEnd = x + offset;
    int yEnd = y + offset;
    int n = a.length;
    int m = a[0].length;

    if (xStart < 0) {
      xStart = 0;
    }
    if (xEnd >= n) {
      xEnd = n - 1;
    }

    if (yStart < 0) {
      yStart = 0;
    } 
    if (yEnd >= m) {
      yEnd = m - 1;
    }

    for (int i = xStart; i <= xEnd; i++) {
      for (int j = yStart; j <= yEnd; j++) {
        if (x == i && y == j) continue;
        a[i][j] = 1;
      }
    }
  }

  static void formatDungeon(int[][] a) {
    int n = a.length;
    int m = a[0].length;

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (a[i][j] != 1 & a[i][j] != 0) {
          increaseMonsterGaze(a, i, j);
        }
      }
    }
  }

  static void printDungeon(int[][] a) {
    for (int[] level : a) {
      System.out.println(Arrays.toString(level));
    }
    System.out.println();
  }
  
  static boolean isValidPlace(int[][] a, int[][] sol, int x, int y) {
    int n = a.length;
    int m = a[0].length;
    return (((0 <= x && x < n) && (0 <= y && y < m)) && a[x][y] == 0 && sol[x][y] != -1);
  }

  static int[] escapeDungeonLevel(int[][] dungeon, int x, int y) {
    
    return dungeon[0];
  }

  static void escapeTheDungeon(int[][] dungeon, int x, int y) {}

  public static void main(String[] args) {
    int[][][] dungeon = {
      {
        { 0, 0, 0, 0, 2, 0 },
        { 0, 1, 0, 0, 0, 0 },
        { 0, 0, 0, 0, 1, 0 },
        { 0, 0, 0, 0, 2, 0 },
        { 0, 0, 0, 0, 0, 0 },
        { 0, 0, 0, 0, 0, 0 },
        { 2, 0, 0, 0, 0, 0 },
      },
      {
        { 0, 0, 0, 0, 0, 2 },
        { 0, 1, 0, 0, 0, 0 },
        { 0, 0, 0, 0, 1, 0 },
        { 0, 0, 0, 0, 0, 0 },
        { 0, 0, 0, 0, 0, 0 },
        { 0, 0, 0, 0, 0, 0 },
        { 3, 0, 0, 0, 0, 0 },
      },
    };
    for (int i = 0; i < dungeon.length; i++) {
      formatDungeon(dungeon[i]);
      printDungeon(dungeon[i]);
    }
  }
}
