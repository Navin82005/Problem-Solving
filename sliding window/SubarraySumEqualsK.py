from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        l, r = 0, 0
        n = len(nums)
        sub_array = 0

        while r < n:
            current_sum += nums[r]
            
            while current_sum > k:
                current_sum -= nums[l]
                l += 1
            sub_array += (r - l + 1)
            r += 1
        
        r = l = current_sum = 0
        while r < n:
            current_sum += nums[r]
            
            while current_sum > k - 1:
                current_sum -= nums[l]
                l += 1
            sub_array -= (r - l + 1)
            r += 1
        
        return sub_array

print(Solution().subarraySum([-1,-1,1].index(5), 0))