class Solution:
    @staticmethod
    def alphabetToKeypadNumbers(word: str) -> str:
        keybinding = {
            "abc": "2",
            "def": "3",
            "ghi": "4",
            "jkl": "5",
            "mno": "6",
            "pqrs": "7",
            "tuv": "8",
            "wxyz": "9"
        }

        
        num = ""
        
        for i in word:
            for j in keybinding:
                if i in j:
                    num = num + keybinding[j]
        
        return num
    
print(Solution.alphabetToKeypadNumbers(word="amazon"))