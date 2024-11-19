class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sM = {}
        tM = {}
        for i in range(len(s)):
            if s[i] not in sM:
                sM[s[i]] = t[i]
            else:
                if sM[s[i]] != t[i]:
                    return False
            if t[i] not in tM:
                tM[t[i]] = s[i]
            else:
                if tM[t[i]] != s[i]:
                    return False

        return True