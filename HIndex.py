class Solution:
    def hIndex(self, citations: List[int]) -> int:

        '''
        [6,5,3,1,0]
         0 1 2 3 4
         1 2 3 4 5
        [3,1,1]
         0 1 2
         1 2 3 
        
        '''
        citations.sort(reverse = True)
        ans = 0
        for i, c in enumerate(citations):
            if  c >= i+1:
                ans = i+1
        return ans
