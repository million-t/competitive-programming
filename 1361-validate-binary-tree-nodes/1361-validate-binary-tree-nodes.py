class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        indegree = defaultdict(int)
        
        for node in range(n):
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    indegree[child] += 1
            
        
        queue = deque()
        for node in range(n):
            if not indegree[node]:
                queue.append(node)
            
            elif indegree[node] > 1:
                return False
        
        order = []
        if len(queue) != 1:
            return False
        
        while queue:
            cur = queue.popleft()
            
            order.append(cur)
            
            for child in [leftChild[cur], rightChild[cur]]:
                if child != -1:
                    indegree[child] -= 1
                    if not indegree[child]:
                        queue.append(child)
                        
            
        
        return len(order) == n
            
            