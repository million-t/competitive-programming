class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append((scores[b], b))
            graph[b].append((scores[a], a))
        
        for node in graph:
            graph[node].sort(reverse = True)
        
        def findTwoExclusive(u, v):
            res = []
            
            for neigh in graph[u]:
                if neigh[1] != v:
                    res.append(neigh)
                
                if len(res) == 2:
                    break
            
            return res
        
        
        ans = -1
        for a, b in edges:
            tempa = findTwoExclusive(a, b)
            tempb = findTwoExclusive(b, a)
            if not tempa or not tempb:
                continue
            
            if (len(tempa) == 1 and len(tempb) == 1) and tempa[0][1] == tempb[0][1]:
                continue
            
            if len(tempa) == len(tempb):
                if tempa[0][1] == tempb[0][1]:
                    if tempa[1][0] >= tempb[1][0]:
                        ans = max(ans, tempa[1][0] + tempb[0][0] + scores[a] + scores[b])
                    
                    else:
                        ans = max(ans, tempb[1][0] + tempa[0][0] + scores[a] + scores[b])
                else:
                    ans = max(ans, tempa[0][0] + tempb[0][0] + scores[a] + scores[b])
            
            elif len(tempa) == 1:
                if tempa[0][1] == tempb[0][1]:
                    ans = max(ans, tempa[0][0] + tempb[1][0] + scores[a] + scores[b])
                else:
                    ans = max(ans, tempa[0][0] + tempb[0][0] + scores[a] + scores[b])
            
            else:
                if tempa[0][1] == tempb[0][1]:
                    ans = max(ans, tempb[0][0] + tempa[1][0] + scores[a] + scores[b])
                else:
                    ans = max(ans, tempa[0][0] + tempb[0][0] + scores[a] + scores[b])
                    
        return ans
                
            
            
            