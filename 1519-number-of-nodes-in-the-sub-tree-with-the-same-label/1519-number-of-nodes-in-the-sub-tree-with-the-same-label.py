class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set([0])
        ans = [0]*n

        def dfs(node):
            
            count = Counter()
            for child in graph[node]:
                
                if child not in visited:
                    visited.add(child)
                    for key, val in dfs(child).items():
                        count[key] += val
            
            count[labels[node]] += 1
            ans[node] = count[labels[node]]
            
            return count
        
        dfs(0)
        return ans