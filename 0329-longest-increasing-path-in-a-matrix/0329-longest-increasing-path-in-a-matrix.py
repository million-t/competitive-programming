class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        rows, cols = len(matrix), len(matrix[0])
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for row in range(rows):
            for col in range(cols):
                node = (row, col)
                
                for neigh in [(row - 1, col), (row, col - 1)]:
                    nr, nc = neigh
                    if nc < 0 or nr < 0:
                        continue
                    
                    if matrix[nr][nc] > matrix[row][col]:
                        graph[node].append(neigh)
                        indegree[neigh] += 1
                    
                    elif matrix[nr][nc] < matrix[row][col]:
                        graph[neigh].append(node)
                        indegree[node] += 1
                        
        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if not indegree[(row, col)]:
                    queue.append((row, col))
        
        steps = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                
                for neigh in graph[cur]:
                    indegree[neigh] -= 1
                    if not indegree[neigh]:
                        queue.append(neigh)
            
            steps += 1
        
        return steps