class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.minHeap, num)
        
        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -1*(heapq.heappop(self.minHeap)))
        
        
        while self.minHeap and self.maxHeap and -1*(self.maxHeap[0]) > self.minHeap[0]:
            
            _min = -1*(heapq.heappop(self.minHeap))
            _max = -1*(heapq.heappop(self.maxHeap))
            
            heapq.heappush(self.minHeap, _max)
            heapq.heappush(self.maxHeap, _min)
            
            
    def findMedian(self) -> float:
        
        if len(self.maxHeap) > len(self.minHeap):
            return -1*(self.maxHeap[0])
        
        return (self.minHeap[0] - (self.maxHeap[0]))/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()