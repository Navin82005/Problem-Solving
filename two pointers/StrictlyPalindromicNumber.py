class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def check_base_palindrome(num, base):
            base_num = ""
            while num > 0:
                base_num = f"{num % base}" + base_num
                num //= base
            return base_num == base_num[::-1]

        for i in range(2, n - 1):
            if not check_base_palindrome(n, i):
                return False
            
        return True
