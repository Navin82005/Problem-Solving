class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tmp = []
        if len(s) != len(t):
            return False
        for i in s:
            if i in t and i not in tmp:
                tmp += [i]
                if t.count(i) != s.count(i):
                    return False
            if i not in t:
                return False

        return True
        # return Counter(s) == Counter(t)