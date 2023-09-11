class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        temp = []
        for ind, num in enumerate(groupSizes):
            temp.append((num, ind))
            
        temp.sort()
        length = len(temp)
        start = end = 0
        
        groups = []
        while start < length:
            
            inc = temp[start][0]
            end = start + inc
            group = [temp[start][1]]
            start += 1
            
            while start < end:
                group.append(temp[start][1])
                start += 1
            
            groups.append(group)
        
        return groups