class Solution:
    def mergeOverlap(self, arr):
        arr.sort()
        t = []
        for i in arr:
            t += [list(range(i[0], i[1] + 1))]
        
        for i in range(len(t) - 1):
            if not set(t[i]).isdisjoint(set(t[i + 1])):
                t[i + 1] = set(t[i]).union(set(t[i + 1]))
                t[i] = 0
            else:
                i += 1

        s = []
        for i in t:
            if i != 0:
                tmp = list(i)
                s += [[min(tmp), max(tmp)]]
        
        return s

# print(Solution().mergeOverlap([[1,3],[2,4],[6,8],[9,10]]))
# print(Solution().mergeOverlap([[9,10],[11,15],[13,15],[16,17], [1, 17], [2, 5]]))
print(Solution().mergeOverlap([[39,54],[49,61],[94,98],[48,56], [28, 47], [87, 95]]))

# 6
# 39 54
# 49 61
# 94 98
# 48 56
# 28 47
# 87 95
