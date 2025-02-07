from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def all_0(count):
            for i in count:
                if count[i] > 0:
                    return False
            return True
        
        n = len(s)
        if n < len(t):
            return ""
        if t in s:
            return t
        
        dic = Counter(t)
        req = len(dic)
        l = 0
        r = 0
        
        window = {}
        min_l = float('inf')
        counter = {}
        res = [-1, -1]
        current = 0
        
        while r < n:
            c = s[r]
            dic[c] = window.get(c, 0) + 1
            
            if c in window and dic[c] == window[c]:
                current += 1
            
            while l < r and s[l] in window and window[s[l]] == dic[c]:
                l += 1
            
            if r - l + 1 < min_l:
                min_l = r - l + 1
                res = [l, r]
            
            
            
            r += 1
        
        return "" if res[0] == -1 else s[res[0]: res[1] + 1]

# print(Solution().minWindow("bba", "ab"))
print(Solution().minWindow("ADOBECODEBANC", "ABC"))