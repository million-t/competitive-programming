class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        rooms_heap = list(range(n))
        meetings_heap = []
        meetings.sort()
        usage = [0]*n
        
        for start, end in meetings:
            
            while meetings_heap and meetings_heap[0][0] <= start:
                finished, room = heappop(meetings_heap)
                heappush(rooms_heap, room)
            
            if not rooms_heap:
                finished, room = heappop(meetings_heap)
                usage[room] += 1
                heappush(meetings_heap, (finished + end - start, room))
            
            else:
                room = heappop(rooms_heap)
                usage[room] += 1
                heappush(meetings_heap, (end, room))
        
        
        _max = max(usage)
        
        for indx, count in enumerate(usage):
            if count == _max:
                return indx
            
        