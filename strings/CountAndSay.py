class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        def rel(elm):
            tmp = ""
            cnt = 0
            ln = len(elm)
            i = 0
            while i < ln:
                cnt = 1
                while i < ln - 1 and elm[i] == elm[i + 1]:
                    cnt += 1
                    i += 1
                tmp += f"{cnt}{elm[i]}"
                i += 1
            return tmp

        dp = ["1"]
        for i in range(n - 1):
            dp.append(rel(dp[i]))
        return dp[-1]
        