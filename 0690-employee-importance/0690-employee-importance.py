"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        
        for emp in employees:  
            graph[emp.id].extend([emp.subordinates, emp.importance])
            
        
        
        def dfs(node):
            
            sub_imp = graph[node][1]
            for subordinate in graph[node][0]:
                sub_imp += dfs(subordinate)
            
            return sub_imp
        
        
        return dfs(id)
                    
                    
                    
                
                    
        