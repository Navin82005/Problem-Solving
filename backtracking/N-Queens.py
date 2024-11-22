from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        def isValidCoordinate(x, y):
            return 0 <= x < n and 0 <= y < n
        
        def checkIfSafe(sol, row, col):
            # print(f"Row = {row}, col = {col}")
            for i in range(row):
                if sol[i][col] == 'Q':
                    return False
            
            for i in range(1, row + 1):
                # print(f"Upper left diagonal: x = {row - i} y = {col - i}")
                if isValidCoordinate(row - i, col - i) and sol[row - i][col - i] == 'Q':
                    return False
            
            for i in range(1, row + 1):
                # print(f"Upper right diagonal: x = {row - i} y = {col + i}")
                if isValidCoordinate(row - i, col + i) and sol[row - i][col + i] == 'Q':
                    return False
            
            return True
        
        def solve(sol, x):
            if n == x:
                # print(sol)
                solutions.append(["".join(row) for row in sol])
                return
            
            for col in range(n):
                if checkIfSafe(sol, x, col):
                    sol[x][col] = "Q"
                    # print(sol, x)
                    solve(sol, x + 1)
                    sol[x][col] = "."
                    
        sol = [["." for _ in range(n)] for __ in range(n)]
        solve(sol, 0)
        
        return solutions
    
print(Solution().solveNQueens(n = 4))