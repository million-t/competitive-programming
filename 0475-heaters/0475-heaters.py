class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        heaters.append(float('inf'))
        
        houses.sort()
        heaters.sort()
        heater_indx = 0
        
        radius = defaultdict(int)
        
        for house in houses:
            while abs(house - heaters[heater_indx]) >= abs(house - heaters[heater_indx + 1]):
                heater_indx += 1
                
            
            radius[heaters[heater_indx]] = max(radius[heaters[heater_indx]], abs(house - heaters[heater_indx]))
                
            
        return max(radius.values())