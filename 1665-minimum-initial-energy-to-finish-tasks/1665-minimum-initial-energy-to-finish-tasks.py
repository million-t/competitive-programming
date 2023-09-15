class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        temp = []
        for act, _min in tasks:
            temp.append((_min - act, _min, act))
        
        temp.sort(reverse = True)
        cost = 0
        spare = 0
        
        for dif, _min, act in temp:
            if spare <= _min:
                cost += _min - spare
                spare = dif
                        
            else:
                spare -= act
        
        return cost
        
        