class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        length = len(requests)
        transfer = defaultdict(int)
        max_achievable = 0
        
        def backtrack(start, transfered):
            nonlocal length, max_achievable
            
            
            for index in range(start, length):
                _from, to = requests[index]
                
                if _from != to:
                
                    transfer[_from] -= 1
                    transfer[to] += 1


                    backtrack(index + 1, transfered + 1)

                    transfer[_from] += 1
                    transfer[to] -= 1
                
                else:
                    transfered += 1
            
            
            if not any(transfer.values()):
                max_achievable = max(max_achievable, transfered)
    
        backtrack(0, 0)
        
        return max_achievable
                
                
                
        
        