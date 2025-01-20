class LargestRectangleInHistogram:
    def findArea(self, histogram):
        max_area = 0
        stack = []
        n = len(histogram)
        
        for i in range(len(histogram)):
            start = i
            while stack and stack[-1][1] > histogram[i]:
                idx, height =  stack.pop()
                max_area = max(max_area, (i - idx) * height)
                start = idx
            stack.append([start, histogram[i]])
        # print(stack)
        
        for i in range(len(stack)):
            max_area = max(max_area, (n - stack[i][0]) * stack[i][1])
        
        return max_area

print(LargestRectangleInHistogram().findArea([2, 1, 5, 6, 2, 3]))

class AreaMaxRectangle:
    def findMaxArea(self, maze):
        n = len(maze)
        m = len(maze[0])
        
        dp = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i + 1 < n:
                    # if (maze[i + 1][j] - maze[i][j]) == 1:
                    if (maze[i + 1][j] == maze[i][j]):
                        dp[i + 1][j] = dp[i][j] + 1
                if j + 1 < m:
                    if maze[i][j + 1] == maze[i][j]:
                        dp[i][j + 1] = dp[i][j] + 1
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if i - 1 >= 0:
                    if maze[i - 1][j] == maze[i][j]:
                        dp[i - 1][j] = max(dp[i - 1][j], dp[i][j] + 1)
                if j - 1 >= 0:
                    if maze[i][j - 1] == maze[i][j]:
                        dp[i][j - 1] = max(dp[i][j - 1], dp[i][j] + 1)
        print(dp)

print(AreaMaxRectangle().findMaxArea([
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0],
]))

# print(AreaMaxRectangle().findMaxArea([
#     [10, 11, 107, 20],
#     [7, 33, 106, 21],
#     [34, 35, 105, 22],
#     [101, 102, 104, 103],
# ]))
