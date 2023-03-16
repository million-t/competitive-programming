class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        time_before_bloom = []
        
        for planting, growing in zip(plantTime, growTime):
            time_before_bloom.append((growing, planting))
        
        
        time_before_bloom.sort( reverse=True )
        
        max_days = 0
        planting_days = 0
        
        for grow_time, plant_time in time_before_bloom:
            planting_days += plant_time
            max_days = max(max_days, planting_days + grow_time)
        
        return max_days
                