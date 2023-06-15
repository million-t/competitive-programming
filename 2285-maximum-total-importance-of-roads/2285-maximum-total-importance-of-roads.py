class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
        indegree = [0]*n
        for a, b in roads:
            indegree[a] -= 1            
            indegree[b] -= 1
        
        heap = []
        for cit, indeg in enumerate(indegree):
            heappush(heap, (indeg, cit))
        
        cities = [0]*n
        
        for num in range(n, 0, -1):
            cities[heappop(heap)[1]] = num
        
        ans = 0
        for a, b in roads:
            ans += cities[a] + cities[b]
        
        return ans

            
        