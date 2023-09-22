class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        
        length = len(people)
        people = [(val, ind) for ind, val in enumerate(people)]
        people.sort()
        vals = [val for val, ind in people]
        inds = [ind for val, ind in people]

        preffix_array = [0]*(length + 1)
        
        for start, end in flowers:
            left = bisect_left(vals, start)
            right = bisect_right(vals, end)
            
            preffix_array[left] += 1
            preffix_array[right] -= 1
            
        for ind in range(1, length + 1):
            preffix_array[ind] += preffix_array[ind - 1]
        
        ans = [0]*length
        for ind in range(length):
            ans[inds[ind]] = preffix_array[ind]
        
        return ans
        
        
        
                
        