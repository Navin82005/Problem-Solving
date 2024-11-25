class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [0, 1]
        while n:
            dp.append(dp[-2] + dp[-1])
            n -= 1
        return dp[-1]
