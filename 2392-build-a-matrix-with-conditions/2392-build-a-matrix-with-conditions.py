class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def topoSort(conditions):
            graph = {num: [] for num in range(1, k + 1)}
            indegree = defaultdict(int)

            for above, below in conditions:
                graph[above].append(below)
                indegree[below] += 1

            topoOrder = []
            queue = deque()

            for num in range(1, k + 1):
                if not indegree[num]:
                    queue.append(num)


            while queue:
                size = len(queue)

                for _ in range(size):
                    cur = queue.popleft()
                    topoOrder.append(cur)

                    for neigh in graph[cur]:
                        indegree[neigh] -= 1
                        if not indegree[neigh]:
                            queue.append(neigh)
            
            return topoOrder
        
        rowTopoOrder = topoSort(rowConditions)
        if len(rowTopoOrder) != k:
            return []
        
        colTopoOrder = topoSort(colConditions)
        if len(colTopoOrder) != k:
            return []
        
        matrix = [[0]*k for row in range(k)]
        num_row = {num: ind for ind, num in enumerate(rowTopoOrder)}
        
        for col, num in enumerate(colTopoOrder):
            row = num_row[num]
            matrix[row][col] = num
        
        return matrix