class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        temp = [(a - b, a, b) for a, b in costs]
        temp.sort()
        length = len(temp)
        
        ans = [0, 0]
        for indx in range(length):
            city = int(indx >= length//2)
            ans[city] += temp[indx][city + 1]
        
        return sum(ans)
        