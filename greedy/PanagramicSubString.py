s = input()

class Solution():
    @staticmethod
    def solve(s: str):
        n = len(s)
        if n < 26:
            return -1
        s = list(s)
        alph = "abcdefghijklmnopqrstuvwxyz"
        for i in alph:
            if i not in s:
                index = s.index("?")
                if index == -1:
                    return -1
                else:
                    s[index] = i
        
        if s.count("?") > 0:
            for i in range(n):
                if s[i] == "?":
                    s[i] = s[i + 1]
            
        return "".join(s)

print(Solution.solve(s))