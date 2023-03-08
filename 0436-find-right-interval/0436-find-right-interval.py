class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        length = len(intervals)
        for i in range(length):
            intervals[i].append(i)
            
        intervals.sort()
        res = [-1]*length
        
        i = 0
        
        for start, end, index in intervals:
            temp = bisect_left(intervals, [end], i , length)
            
            if temp != length:
                res[index] = intervals[temp][2]
                
            i += 1
            
        return res