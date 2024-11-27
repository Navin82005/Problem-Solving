from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        if 1 in nums:
            return 1
        min_val = float('inf')
        for i in nums:
            diff = abs(i)
            if diff < abs(min_val):
                min_val = i
            elif diff == abs(min_val):
                min_val = max(i, min_val)
        return min_val
    
# Possible testcases
print(Solution().findClosestNumber([-4,-2,1,4,8]))
print(Solution().findClosestNumber([2,-1,1,1]))
print(Solution().findClosestNumber([2,1,1,-1,100000]))
