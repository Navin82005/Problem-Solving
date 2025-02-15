import heapq


class MaximumKSums:
    def findMaximumKSums(self, a: list, b: list, k: int) -> list:
        def sortK(a):
            for idx in range(k):
                max_idx = idx
                for jdx in range(idx + 1, n):
                    if a[jdx] > a[max_idx]:
                        max_idx = jdx
                a[idx], a[max_idx] = a[max_idx], a[idx]
            return a
        
        n = len(a)
        if n != len(b):
            return []
        
        a = sortK(a)
        b = sortK(b)
        print(a, b)
        
        res = []
        for idx in range(k):
            for jdx in range(k):
                res += [a[idx] + b[jdx]]
        
        heapq._heapify_max(res)
        return heapq.nlargest(k, res)

print(MaximumKSums().findMaximumKSums([1, 2, 5, 4, 4, 1], [1, 2, 5, 4, 4, 1], 3))