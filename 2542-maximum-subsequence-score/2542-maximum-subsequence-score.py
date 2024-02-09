class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        temp = sorted(zip(nums2, nums1))
        heap = []
        
        for indx in range(len(nums1) - 1, len(nums1) - k - 1, -1):
            heappush(heap, temp[indx][1])
        
        _sum = sum(heap)
        ans = _sum*temp[-k][0]
        
        for indx in range(len(nums1) - k -1, -1, -1):
            if heap[0] < temp[indx][1]:
                _sum += temp[indx][1] - heappop(heap)
                heappush(heap, temp[indx][1])
                ans = max(ans, _sum*temp[indx][0])
                
        return ans
        
        
        
        