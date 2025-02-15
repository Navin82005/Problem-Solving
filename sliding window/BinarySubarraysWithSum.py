from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        current_sum = 0
        l, r = 0, 0
        n = len(nums)
        sub_array = 0
        
        # if set(nums) == set([0]):
        #     return (n * (n + 1)) // 2

        while r < n:
            current_sum += nums[r]
            
            while current_sum > goal:
                current_sum -= nums[l]
                l += 1
            sub_array += (r - l + 1)
            r += 1
        
        if goal != 0:
            r = l = current_sum = 0
            while r < n:
                current_sum += nums[r]
                
                while current_sum > goal - 1:
                    current_sum -= nums[l]
                    l += 1
                sub_array -= (r - l + 1)
                r += 1
        
        return sub_array

# print(Solution().numSubarraysWithSum([1,0,1,0,1], 2))
print(Solution().numSubarraysWithSum([0, 1, 0, 1, 0], 2))