from typing import List


class Solution:
    @staticmethod
    def findMatrix(nums: List[int]) -> List[List[int]]:
        lst = [[]]
        nums.sort()
        for i in range(len(nums)):
            if (nums[i - 1] != nums[i]):
                k = 0
            try:
                lst[k] += [nums[i]]
                k += 1
            except IndexError:
                lst += [[nums[i]]]
                k += 1
        return lst

print(Solution.findMatrix([1,3,4,1,2,3,1]))