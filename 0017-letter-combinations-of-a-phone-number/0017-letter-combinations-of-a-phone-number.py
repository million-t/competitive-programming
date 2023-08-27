class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        keypad = {
            '2': 'abc',
            '3': 'def',
        
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        length = len(digits)
        ans = []
        
        def backtrack(ind, arr, length):
            if ind >= length:
                comb = ''.join(arr)
                if len(comb) > 0:
                    ans.append(comb)
                return
            
            for char in keypad[digits[ind]]:
                arr.append(char)
                backtrack(ind + 1, arr, length)
                arr.pop()
        
        backtrack(0, [], length)
        return ans