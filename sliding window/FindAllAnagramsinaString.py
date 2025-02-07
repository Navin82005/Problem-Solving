from collections import Counter
from typing import List

# BRUTEFORCE SOLUTIONS
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         res = []
#         k = len(p)
#         n = len(s)
#         i = 0
#         p = list(p)
#         p.sort()
#         while i < n - k + 1:
#             window = s[i: i + k]
#             window = sorted(window)
#             # print(window)
#             if window == p:
#                 res.append(i)
#             i += 1
#         return res

# OPTIMAL SOLUTION
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        l = 0
        n = len(s)
        k = len(p)
        r = k
        dic_p = Counter(p)
        window = Counter(s[:k])
        
        while r <= n:
            if dic_p == window:
                res.append(l)
            
            window[s[l]] -= 1
            if window[s[l]] <= 0:
                window.pop(s[l])
            
            if r < n:
                window[s[r]] += 1

            r += 1
            l += 1

        return res
