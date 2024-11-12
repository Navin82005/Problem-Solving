from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        mod = []
        neg = 0
        pos = 0
        n = len(nums)

        def isNegative(num):
            return num < 0

        def findNextPos(s):
            print("list(s, n): ", list(range(s, n)))
            for i in range(s, n):
                if not isNegative(nums[i]):
                    return nums[i], i + 1
            return 0, 0
        
        def findNextNeg(s):
            for i in range(s, n):
                if isNegative(nums[i]):
                    return nums[i], i + 1
            return 0, 0
        

        while neg < n and pos < n:
            res, pos = findNextPos(pos)
            print("Pos:", pos)
            mod.append(res)
            res, neg = findNextNeg(neg)
            print("Neg:", neg)
            mod.append(res)
        
        return mod

print(Solution().rearrangeArray([3,1,-2,-5,2,-4]))