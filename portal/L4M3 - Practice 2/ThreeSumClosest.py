from typing import List


class Solution:
    @staticmethod
    def threeSumClosest(tar: int, nums: List[int]) -> int:
        max_sum = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] >= max_sum and nums[i] + nums[j] + nums[k] <= tar:
                        max_sum = nums[i] + nums[j] + nums[k]
        
        return max_sum

print(Solution.threeSumClosest(2, [-7, 9, 8, 3, 1, 1]))