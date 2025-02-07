class Solution:
    def can_sum(self, target: int, lst: list[int]) -> bool:
        dp = [False for _  in range(target + 1)]
        min_lst = [[0] for _ in range(target + 1)]
        
        for i in range(target + 1):
            for j in lst:
                if i + j <= target and sum(min_lst[i]) + j == j:
                    print(min_lst[i], j, min_lst)
                    min_lst[i + j] = [*min_lst[i], j]
        print(min_lst)
        return False

print(Solution().can_sum(7, [1, 2, 3, 4, 5, 6, 7]))