class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        graph = defaultdict(list)
        
        for ind, route in enumerate(routes):    
            for city in route:
                graph[city].append(ind)
        
        
        queue = deque([source])
        visited = set([source])
        visited_ind = set()
        
        buses = 0
        while queue:
            
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
            
                if cur == target:
                    return buses
                
                for neighs_ind in graph[cur]:
                    
                    if not neighs_ind in visited_ind:
                        visited_ind.add(neighs_ind)
                        
                        for city in routes[neighs_ind]:
                        
                            if city not in visited:
                                visited.add(city)
                                queue.append(city)
                            
            
            buses += 1
        
        return -1