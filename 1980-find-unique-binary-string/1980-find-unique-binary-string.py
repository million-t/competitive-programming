class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        
        seen = set(nums)
        self.ans = ""
        
        def backtrack(bits):
            if self.ans:
                return
            
            if len(bits) == len(nums):
                temp = "".join(bits)
                if temp not in seen:
                    self.ans = temp
                
                return
            
            for bit in ['0', '1']:
                bits.append(bit)
                backtrack(bits)
                bits.pop()
        
        backtrack([])
        return self.ans