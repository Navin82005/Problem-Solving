class AntPathProblem:
    def findTheMaxLength(self, maze):
        n = len(maze)
        m = len(maze[0])
        
        dp = [[1] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i + 1 < n:
                    if (maze[i + 1][j] - maze[i][j]) == 1:
                        dp[i + 1][j] = dp[i][j] + 1
                if j + 1 < m:
                    if maze[i][j + 1] - maze[i][j] == 1:
                        dp[i][j + 1] = dp[i][j] + 1
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i - 1 >= 0:
                    if maze[i - 1][j] - maze[i][j] == 1:
                        dp[i - 1][j] = max(dp[i - 1][j], dp[i][j] + 1)
                if j - 1 >= 0:
                    if maze[i][j - 1] - maze[i][j] == 1:
                        dp[i][j - 1] = max(dp[i][j - 1], dp[i][j] + 1)
        print(dp)

print(AntPathProblem().findTheMaxLength([
    [1, 2, 7],
    [2, 3, 6],
    [4, 4, 5],
]))

print(AntPathProblem().findTheMaxLength([
    [10, 11, 107, 20],
    [7, 33, 106, 21],
    [34, 35, 105, 22],
    [101, 102, 104, 103],
]))
