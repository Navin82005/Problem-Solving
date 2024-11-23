class Solution:
    @staticmethod
    def isPerfect(num: int) -> bool:
        tar = 0
        for i in range(1, num):
            if num % i == 0:
                tar += i
        
        return tar == num

t = int(input())

for _ in "*" * t:
    print("YES" if Solution.isPerfect(int(input())) else "NO")
