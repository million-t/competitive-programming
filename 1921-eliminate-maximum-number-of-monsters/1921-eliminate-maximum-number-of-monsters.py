class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        motion = sorted([d/v for d, v in zip(dist, speed)])
        kills = 0
        
        for time, reach_time in enumerate(motion):
            if time >= reach_time:
                return kills
            
            kills += 1
        
        return kills