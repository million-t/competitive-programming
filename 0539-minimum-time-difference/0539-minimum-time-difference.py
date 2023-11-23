class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        def findDif(a, b):
            a = a.split(":")
            b = b.split(":")
            
            dif = (int(b[0]) - int(a[0]))*60 + int(b[1]) - int(a[1])
            alt = (-int(b[0]) + int(a[0]) + 24)*60 - int(b[1]) + int(a[1])
            return min(alt, dif)
        
        timePoints.sort()
        min_dif = findDif(timePoints[0], timePoints[-1])
        
        for indx in range(1, len(timePoints)):
            min_dif = min(min_dif, findDif(timePoints[indx - 1], timePoints[indx]))
        
        return min_dif