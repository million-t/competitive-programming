
class ThroneInheritance:
    
    

    def __init__(self, kingName: str):
        self.family_tree = defaultdict(list)
        self.king = kingName
        self.dead = set()
        
    def birth(self, parentName: str, childName: str) -> None:
        
        self.family_tree[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.dead.add(name)

        
    def getInheritanceOrder(self) -> List[str]:
        order = []
        
        stack = [self.king]
        
        while stack:
            cur_person = stack.pop()
            
            if cur_person not in self.dead:
                order.append(cur_person)
            
            for child in self.family_tree[cur_person][::-1]:
                stack.append(child)
        
        return order
        
        
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()