class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        
        prev_num = arr[0]
        wins = 0
        
        for indx in range(1, len(arr)):
            num = arr[indx]
            
            if num > prev_num:
                wins = 1
                prev_num = num
            
            else:
                wins += 1
            
            if wins == k:
                return prev_num
        
        
        return max(arr)
        