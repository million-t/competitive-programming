class Solution:
    
    def topoSort(self, graph, indegree):
        
        topoOrder = []
        queue = deque()
        for node in graph:
            if not  indegree[node]:
                queue.append(node)
        
        while queue:
            size = len(queue)
        
            for  _ in range(size):
                cur = queue.popleft()
                topoOrder.append(cur)
                
                for neigh in graph[cur]:
                    indegree[neigh] -= 1
                    if not indegree[neigh]:
                        queue.append(neigh)
                        
        return topoOrder
    
    
    
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        gr_count = defaultdict(int)
        group_less = -1
        
        for ind in range(n):
            if group[ind] == -1:
                group[ind] = group_less
                group_less -= 1
            
            gr_count[group[ind]] += 1
            
        
        group_graph = defaultdict(set)
        # group_incomings = defaultdict(set)
        group_indegree = defaultdict(int)
        graph = defaultdict(lambda: defaultdict(list))
        indegree = defaultdict(int)
        seen = set()
        
        for node, preced in enumerate(beforeItems):
            gn = group[node]
            if not group_graph[gn]:
                group_graph[gn] = set()
            
            if not graph[gn][node]:
                graph[gn][node] = []
                
                
            for vertex in preced:
                
                gv = group[vertex]
                if gv != gn:
                    group_graph[gv].add(gn)
                    if (gv, gn) not in seen: 
                        group_indegree[gn]  += 1
                        seen.add((gv, gn))
                
                else:
                    graph[gn][vertex].append(node)
                    indegree[node] += 1
                    
            
        # for node, incoming in group_incomings.items():
        #     group_indegree[node] = len(incoming)
            
        # print(group_graph)
        # print(group_indegree)

        
        ans = [-1]*n
        group_order = self.topoSort(group_graph, group_indegree)
        # print(group_order)
        if len(group_order) < len(group_graph):
            return []
        
        ans = []
        for gr in group_order:
            
            if graph[gr]:
                for next_node in self.topoSort(graph[gr], indegree):
                    ans.append(next_node)
        
        if len(ans) == n:
            return ans
    
        return []
            
        
        
        
        
        
        