class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        
        
        graph = defaultdict(list)
        
        for (a, b), prob in zip(edges, succProb):
            graph[a].append((b, prob))
            graph[b].append((a, prob))
            
        
        probs = defaultdict(int)
        heap = [(-1, start_node)]
        
        while heap:
            prob, node = heappop(heap)
            prob = -prob
            
            if prob <= probs[node]:
                continue
            
            probs[node] = prob
            
            for neigh, p in graph[node]:
                heappush(heap, (-(prob*p), neigh))
        
        
        return probs[end_node]