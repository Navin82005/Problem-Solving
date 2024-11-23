class Solution:
    @staticmethod
    def findNthFib(n: int) -> int:
        dp = [0, 1]
        
        for i in range(2, n + 2):
            dp.append(dp[i - 2] + dp[i - 1])
        
        tmp = str(dp[n])[-2:]
        if len(tmp) == 1:
            return "0" + tmp
        
        return int(tmp)

print(Solution.findNthFib(n=int(input())))