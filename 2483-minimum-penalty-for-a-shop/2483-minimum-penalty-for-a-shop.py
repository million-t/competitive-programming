class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        
        sufy = customers.count('Y')
        prefn = 0
        penalty = sufy
        ans = 0
        
        for indx, char in enumerate(customers):
            
            if char == 'Y':
                sufy -= 1
            
            else:
                prefn += 1
            
            if sufy + prefn < penalty:
                ans = indx + 1
                penalty = sufy + prefn
                
        return ans
        