class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        last = 0
        ans = 0
        
        for row in range(len(bank)):
            ones = bank[row].count('1')
            ans += last * ones
            if ones:
                last = ones
        
        return ans
            
        