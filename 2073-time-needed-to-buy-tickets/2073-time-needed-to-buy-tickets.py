class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        time_taken = 0
        for i, ticket in enumerate(tickets):
            
            if i <= k:
                time_taken += min(ticket, tickets[k])
            
            else:
                time_taken += min(ticket, tickets[k] - 1)
                
        return time_taken
        