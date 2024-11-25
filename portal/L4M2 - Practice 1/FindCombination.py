num_dict = {
    0: ("zero", 2),
    1: ("one", 2),
    2: ("two", 1),
    3: ("three", 2),
    4: ("four", 2),
    5: ("five", 2),
    6: ("six", 1),
    7: ("seven", 2),
    8: ("eight", 2),
    9: ("nine", 2),
}

class Solution:
    def findCombination(self, lst):
        combinations = []
        
        vowel_count = 0
        for i in lst:
            vowel_count += num_dict[i][0]
        
        def findComb(l, data, start, end, index, r):
            if (index == r and sum(data) == vowel_count):
                combinations.append(data)
            
            i = start
            while i <= end and end - i + 1 >= r - index:
                data[index] = l[i]
                findComb(l, data, i + 1, end, index + 1, r)
                i += 1
        
        # data = [0] * 
        findComb(lst, )
        
        return combinations

print(Solution().findCombination(list(map(int, input().split()))))