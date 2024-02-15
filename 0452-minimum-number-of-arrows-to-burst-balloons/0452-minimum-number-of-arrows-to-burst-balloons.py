class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key= lambda x :(x[1], x[0]))
        ans = 0
        right = 0
        left = 0
        
        while left < len(points):
            while right < len(points) and points[right][0] <= points[left][1]:
                right += 1
            
            ans += 1
            left = right
        
        return ans