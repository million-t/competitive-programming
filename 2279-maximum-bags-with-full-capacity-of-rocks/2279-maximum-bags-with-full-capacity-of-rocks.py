class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        temp = []
        for bag_cap, bag_rocks in zip(capacity, rocks):
            temp.append(bag_cap - bag_rocks)
        
        temp.sort()
        full_count = 0   
        ind = 0
        
        while ind < len(temp) and additionalRocks - temp[ind] >= 0:
            full_count += 1
            additionalRocks -= temp[ind]
            ind += 1
        
        return full_count