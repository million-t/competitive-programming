class DSU:
    def __init__(self, obj):
        
        self.rep = {num: num for num in obj}
        self.rank = {num: 1 for num in obj}
    
    def find(self, x):
        
        root = x
        while root != self.rep[root]:
            root = self.rep[root]
        
        while x != root:
            temp = self.rep[x]
            self.rep[x] = root
            x = temp
        
        return root
    
    def union(self, x, y):
        rep_x = self.find(x)
        rep_y = self.find(y)
        
        if rep_x == rep_y:
            return
        
        if self.rank[rep_x] > self.rank[rep_y]:
            self.rep[rep_y] = rep_x
        
        elif self.rank[rep_x] < self.rank[rep_y]:
            self.rep[rep_x] = rep_y
        
        else:
            self.rep[rep_y] = rep_x
            self.rank[rep_x] += 1
        
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)



class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        
        
        
        meetings.sort(key=lambda x:x[2])
        informed = set([0, firstPerson])
        
        connections = defaultdict(set)
        
        for x, y, time in meetings:
            connections[time].add(x)
            connections[time].add(y)


        indx = 0
        while indx < len(meetings):
            x, y, time = meetings[indx]
            cur_union_find = DSU(connections[time])
            cur_union_find.union(x, y)
            
            while indx + 1 < len(meetings) and meetings[indx][2] == meetings[indx + 1][2]:
                x2, y2, time2 = meetings[indx + 1]
                cur_union_find.union(x2, y2)
                indx += 1
            
            reps = set()
            for person in connections[time]:
                if person in informed:
                    reps.add(cur_union_find.find(person))
            
            for person in connections[time]:
                if cur_union_find.find(person) in reps:
                    informed.add(person)
            
            indx += 1
        
        return list(informed)
                
          
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        