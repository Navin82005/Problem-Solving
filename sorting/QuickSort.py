class QuickSort:
    def quick_sort(self, lst):
        def swap(l, x, y):
            l[x], l[y] = l[y], l[x]
        
        def helper(l, left, right):
            pov = lst[right]
            i = left - 1
            
            for j in range(left, right):
                if lst[j] < pov:
                    i += 1
                    swap(lst, i, j)

            swap(lst, i + 1, right)
            return i + 1

        def _sort_(l, left, right):
            if left < right:
                i = helper(l, left, right)
                _sort_(l, left, i - 1)
                _sort_(l, i + 1, right)
        
        _sort_(lst, 0, len(lst) - 1)
        return lst

print(QuickSort().quick_sort([1, 5, 7, 4, 1, 2, 3]))
