class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        trainers.sort()
        players.sort()
        
        t_size = len(trainers)
        t_ptr = 0
        
        count = 0 
        for p_ptr in range(len(players)):
            while t_ptr < t_size and trainers[t_ptr] < players[p_ptr]:
                t_ptr += 1
            
            if t_ptr < t_size:
                count += 1
                t_ptr += 1
            
        return count