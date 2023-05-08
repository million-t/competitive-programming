class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        supplies = set(supplies)
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for ind in range(len(recipes)):
            for ingredient in ingredients[ind]:
                graph[ingredient].append(recipes[ind])
            
            indegree[recipes[ind]] += len(ingredients[ind])
        
        queue = deque(supplies)

        made = []
        while queue:
            cur = queue.popleft()
            
            if cur not in supplies:
                made.append(cur)
                
            for neigh in graph[cur]:
                indegree[neigh] -= 1
                
                if not indegree[neigh]:
                    queue.append(neigh)
        
        return made