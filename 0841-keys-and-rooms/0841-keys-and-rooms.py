class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        queue = deque([0])
        visited = [0]*len(rooms)
        visited[0] = 1
        
        
        while queue:
            cur = queue.popleft()
            
            for neigh in rooms[cur]:
                if not visited[neigh]:
                    visited[neigh] = 1
                    queue.append(neigh)
            
        
        return all(visited)
            
        