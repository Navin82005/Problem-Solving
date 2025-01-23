def merge_sort(l, left, right):
    def merge(l, left, mid, right):
        n1 = mid - left + 1
        n2 = right - mid
        
        i = 0
        j = 0
        k = left
        # print("OUT OF WHILE:", left, mid, right)
        # print("left sub array:", l[:left])
        # print("right sub array:", l[mid : right])
        
        left_array = l[:left]
        right_array = l[mid: right]
        while i < len(left_array) and j < len(right_array):
            # print(i, j, i + left, j + left, n1, n2, left, mid, right)
            print(left_array, right_array)
            
            if left_array[i] < right_array[j]:
                l[k] = right_array[j]
                i += 1
            else:
                l[k] = right_array[j]
                j += 1
            k += 1
        
    if left < right:
        mid = (left + right) // 2
        
        merge_sort(l, left, mid)
        merge_sort(l, mid + 1, right)
        
        merge(l, left, mid, right)

l = [45, 78, 12, 49, 11, 6]
merge_sort(l, 0, len(l))

print(*l)