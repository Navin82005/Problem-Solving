from collections import defaultdict
from typing import Counter, List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        repeaters = []
        map = defaultdict(lambda: 0)
        for i in range(len(s) - 9):
            tag = s[i: i + 10]
            if tag in map and tag not in repeaters:
                repeaters.append(s[i: i + 10])
            map[tag] += 1
        return repeaters
    
# possible test cases
# print(Solution().findRepeatedDnaSequences(s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
# print(Solution().findRepeatedDnaSequences(s = "AAAAAAAAAAAAA"))
# print(Solution().findRepeatedDnaSequences(s = "AAAAAAAAAAA")) # ["AAAAAAAAAA"]
# print(Solution().findRepeatedDnaSequences(s = "AAAAAAAAAA")) # []