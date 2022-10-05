class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap= []
        for x, y in points:
            minHeap.append([sqrt(x**2 + y**2),[x,y]])
        heapq.heapify(minHeap)

        ans = []
        for i in range(k):
            ans.append(heapq.heappop(minHeap)[1])
        return ans
