class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        temp = defaultdict(list)
        groups = []
        
        for ind, num in enumerate(groupSizes):
            temp[num].append(ind)
            
            if len(temp[num]) == num:
                groups.append(temp[num])
                temp[num] = []
        
        return groups