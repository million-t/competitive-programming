class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        def findDif(a, b):
            dif = (b[0] - a[0])*60 + b[1] - a[1]
            alt = (-b[0] + a[0] + 24)*60 - b[1] + a[1]
            return min(alt, dif)
        
        timePoints.sort()
        for indx in range(len(timePoints)):
            time = timePoints[indx].split(':')
            timePoints[indx] = (int(time[0]), int(time[1]))
            
        min_dif = findDif(timePoints[0], timePoints[-1])
        
        for indx in range(1, len(timePoints)):
            min_dif = min(min_dif, findDif(timePoints[indx - 1], timePoints[indx]))
        
        return min_dif