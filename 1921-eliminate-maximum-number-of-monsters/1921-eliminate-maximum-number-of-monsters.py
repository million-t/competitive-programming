class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = [d/v for d, v in zip(dist, speed)]
        time.sort()
        
        shot = 0
        
        for cur_time, time_left in enumerate(time):
            if time_left <= cur_time:
                break
                
            shot += 1
        
        return shot