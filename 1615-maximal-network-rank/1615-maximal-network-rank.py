class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        degree = defaultdict(int)
        connected = set()
        
        for initial, termin in roads:
            degree[initial] += 1
            degree[termin] += 1
            connected.add((initial, termin))
        
        
        max_rank = 0
        for node1 in range(n):
            for node2 in range(node1 + 1, n):
                
                cur_rank = degree[node1] + degree[node2]
                
                if (node1, node2) in connected or (node2, node1) in connected:
                    cur_rank -= 1
                
                max_rank = max(max_rank, cur_rank)
        
        return max_rank
                
                    