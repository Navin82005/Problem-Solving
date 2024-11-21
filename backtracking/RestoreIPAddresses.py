from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) > 12:
            return res

        def backtracking(i, dots, currIp):
            if dots == 4 and i == len(s):
                res.append(currIp[:-1])
            if dots > 4:
                return
            for j in range(i, min(i + 3, len(s))):
                if int(s[i : j + 1]) < 256 and (i == j or s[i] != "0"):
                    backtracking(j + 1, dots + 1, currIp + s[i : j + 1] + ".")

        backtracking(0, 0, "")
        return res
