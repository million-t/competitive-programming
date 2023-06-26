
    
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:

        
        enemy = defaultdict(set)
        
        
        for x, y in restrictions:
            enemy[x].add(y)
            enemy[y].add(x)
        
        
        
        rep = list(range(n))
        rank = [0]*n
        
        
        ans = []
        def find(x):
        
            root = x
            while root != rep[root]:
                root = rep[root]

            while x != root:
                temp = rep[x]
                rep[x] = root
                x = temp

            return root

        def union(x, y):
            rep_x = find(x)
            rep_y = find(y)
            
            
            for person in enemy[rep_y]:
                if find(person) == rep_x:
                    ans.append(False)
                    return
            
            if rep_x == rep_y:
                ans.append(True)
                return
            
            
            if rank[rep_x] > rank[rep_y]:
                enemy[rep_x].update(enemy[rep_y])
                
                rep[rep_y] = rep_x

            elif rank[rep_x] < rank[rep_y]:
                enemy[rep_y].update(enemy[rep_x])
                rep[rep_x] = rep_y

            else:
                enemy[rep_x].update(enemy[rep_y])
                rep[rep_y] = rep_x
                rank[rep_x] += 1
            
            ans.append(True)
        

        
        for u, v in requests:
            union(u, v)
        
        return ans
    
        
        
        
        
        