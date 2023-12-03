class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        secs = 0
        for indx in range(1, len(points)):
            xi, yi = points[indx]
            xp, yp = points[indx - 1]
            secs += max(abs(xp - xi), abs(yi - yp))
        
        return secs
        