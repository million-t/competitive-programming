class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        def inbound(row, col): return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        graph = defaultdict(list)
        indegree = defaultdict(int)
        cols = len(grid[0])
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
        
                    if inbound(nr, nc) and grid[nr][nc] > grid[row][col]:
                        ind = row*cols + col
                        ni = nr*cols + nc
                        graph[ind].append(ni)
                        indegree[ni] += 1
        
        
        queue = deque()
        for node in graph:
            if not indegree[node]:
                queue.append(node)
        
        
        ans_arr = [1]*(len(grid)*len(grid[0])) 
        mod = 10**9 + 7
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                
                for neigh in graph[node]:
                    ans_arr[neigh] = (ans_arr[neigh] + ans_arr[node])%mod
                    indegree[neigh] -= 1
                    if not indegree[neigh]:
                        queue.append(neigh)
        
        ans = 0
        for num in ans_arr:
            ans = (ans + num)%mod
        
        return ans
                