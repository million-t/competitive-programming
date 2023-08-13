class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        
        s1 = sorted(s1)
        s2 = sorted(s2)
        if s1 > s2:
            s1, s2 = s2, s1
            
            
        for from_s1, from_s2 in zip(s1, s2):
            if from_s1 > from_s2:
                return False
        
        return True
        