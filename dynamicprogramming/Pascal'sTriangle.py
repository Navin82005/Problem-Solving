from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        
        dp = [[1], [1, 1]]
        
        for i in range(numRows):
            tmp = dp[-1]
            tmpL = len(tmp)
            for j in range(1, tmpL):
                # if j == 0 and j == tmpL - 1:
                #     tmp[j] = tmp[j]
                print([tmp[j - 1] + tmp[j]])
                
                tmp = tmp[:j] + [tmp[j - 1] + tmp[j]] + tmp[j:]
            dp.append(tmp)
        return dp

print(Solution().generate(3))