class Solution:
    def isHappy(self, n: int) -> bool:
        def powerNumberAndSum(n: int):
            return sum(int(num) ** 2 for num in str(n))
        l = []
        
        while n not in l and n != 1:
            l.append(n)
            n = powerNumberAndSum(n)
        return n == 1