from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        mapm = {"(":")","{":"}","[":']'}
        for w in s:
            if w=="(" or w=="{" or w=="[":
                q.append(w)
            else:
                if not q:
                    return False
                x=q.pop()
                if w!=mapm[x]:
                    return False
        if q:
            return False
        return True