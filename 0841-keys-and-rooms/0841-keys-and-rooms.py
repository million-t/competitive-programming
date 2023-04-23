class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        stack = [0]
        visited = [0]*len(rooms)
        visited[0] = 1
        
        while stack:
            cur_room = stack.pop()
            
            for key in rooms[cur_room]:
                if not visited[key]:
                    stack.append(key)
                    visited[key] = 1
                    
        return sum(visited) == len(rooms)
        