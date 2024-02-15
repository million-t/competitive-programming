class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        
        ans = 0
        freq = Counter(answers)
        
        for num, count in freq.items():
            ans += max(num + 1, (num + 1)*math.ceil(count/(num + 1)))
        
        return ans
        
            