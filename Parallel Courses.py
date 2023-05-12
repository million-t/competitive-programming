from collections import deque, defaultdict

def parallelCourses(n, prerequisites):
    
    graph = [[] for _ in range(n)] 
    indegree = defaultdict(int)

    for _from, to in prerequisites:
        graph[_from - 1].append(to - 1)
        indegree[to - 1] += 1
    

    queue = deque()
    
    for node in range(n):
        if not indegree[node]:
            queue.append(node)
    
    sems = 0
    count = 0
   
    while queue:

        size = len(queue)
        for _ in range(size):
            cur = queue.popleft()
            count += 1
        
            for neigh in graph[cur]:
                indegree[neigh] -= 1
                if not indegree[neigh]:
                    queue.append(neigh)
            
        sems += 1


    if count == n:
        return sems

    return -1
