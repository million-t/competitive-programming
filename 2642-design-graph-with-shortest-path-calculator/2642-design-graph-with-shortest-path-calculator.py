class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        
        self.size = n
        self.graph = [[] for _ in range(n)]
        for _from, to, cost in edges:
            self.graph[_from].append((to, cost))
        

    def addEdge(self, edge: List[int]) -> None:
        _from, to, cost = edge
        self.graph[_from].append((to, cost))
        

    def shortestPath(self, node1: int, node2: int) -> int:
        
        dist = [float('inf')]*self.size
        heap = [(0, node1)]
        
        while heap:
            cur_dist, cur = heappop(heap)
            
            if cur_dist >= dist[cur]:
                continue
            
            dist[cur] = cur_dist
            for to, cost in self.graph[cur]:
                heappush(heap, (cur_dist + cost, to))
        
        return dist[node2] if dist[node2] != float('inf') else -1
            
            
            


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)