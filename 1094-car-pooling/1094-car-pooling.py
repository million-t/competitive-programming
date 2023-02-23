class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        furthest_place = 0
        for passengers, from_, to in trips:
            furthest_place = max(furthest_place, to)
        
        
        total_journey = [0]*(furthest_place + 1)
        
        for passengers, from_, to in trips:
            total_journey[from_] += passengers
            total_journey[to] -= passengers
            
        for i in range(1, len(total_journey)):
            total_journey[i] += total_journey[i-1]
        
        for passengers in total_journey:
            
            if passengers > capacity:
                return False
            
        return True
            
        