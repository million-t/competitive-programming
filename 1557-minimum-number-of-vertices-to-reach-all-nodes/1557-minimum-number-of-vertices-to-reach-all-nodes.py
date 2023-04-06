class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        indegree = {}
        
        for _from, to in edges:
            indegree[to] = indegree.get(to, 0) + 1
            indegree[_from] = indegree.get(_from, 0) + 0
        
        return [node for node, indeg in indegree.items() if not indeg]
        