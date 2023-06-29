from typing import List
from collections import defaultdict, deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:

        indegree = defaultdict(int)
        for node, neighbors in enumerate(adj):
            for neigh in neighbors:
                indegree[neigh] += 1
        
        queue = deque()
        
        for node in range(V):
            if indegree[node] < 2:
                queue.append(node)

        
        topoCount = 0
        while queue:
            
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                topoCount += 1
                
                
                for neigh in adj[cur]:
                    indegree[neigh] -= 1
                    if indegree[neigh] == 1:
                        queue.append(neigh)
                        
            
        
        return int(topoCount != V)

#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
