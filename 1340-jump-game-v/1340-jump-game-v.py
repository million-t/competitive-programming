class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        

        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        
        
        stack = []
        for ind, num in enumerate(arr):
            
            while stack and ind - stack[-1] <= d and arr[stack[-1]] < num:
                popped = stack.pop()
                graph[ind].append(popped)
                indegree[popped] += 1
                
            stack.append(ind)
        
        stack = []
        for ind in range(len(arr) - 1, -1, -1):
            num = arr[ind]
            while stack and stack[-1] - ind <= d and arr[stack[-1]] < num: 
                popped = stack.pop()
                graph[ind].append(popped)
                indegree[popped] += 1
            
            stack.append(ind)
        
        
        queue = deque()
        for node in range(len(arr)):
            if not indegree[node]:
                queue.append(node)
            
        jumps = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                
                for neigh in graph[cur]:
                    indegree[neigh] -= 1
                    if  not indegree[neigh]:
                        queue.append(neigh)
                        
            jumps += 1
             
            
        return jumps
        
        