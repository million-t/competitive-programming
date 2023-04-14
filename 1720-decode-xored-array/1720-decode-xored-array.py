class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
        
        arr = [first]
        
        for num in encoded:
            arr.append(num^arr[-1])
        
        return arr
        
        