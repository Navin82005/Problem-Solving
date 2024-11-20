from collections import Counter
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        
        if len(word) > n * m:
            return False
        
        board_freq = Counter(sum(board, []))

        for char, count in Counter(word).items():
            if board_freq[char] < count:
                return False
        
        def search(i, j, k):
            if k == len(word):
                return True
            
            if 0 <= i < n and 0 <= j < m and word[k] == board[i][j]:
                tmp = board[i][j]
                board[i][j] = "0"
                if search(i + 1, j, k + 1):
                    return True
                if search(i, j + 1, k + 1):
                    return True
                if search(i - 1, j, k + 1):
                    return True
                if search(i, j - 1, k + 1):
                    return True
                board[i][j] = tmp
                
            return False
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if search(i, j, 0):
                        return True
        return False

# Possible test cases
# print(Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
# print(Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))
# print(Solution().exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"))