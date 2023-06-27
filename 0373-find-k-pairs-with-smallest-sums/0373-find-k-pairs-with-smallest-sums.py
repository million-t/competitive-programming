class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        if not k or not nums1 or not nums2: 
            return []
        
        heap = []
        len1, len2 = len(nums1), len(nums2)
        heappush(heap, (nums1[0] + nums2[0], 0, 0))
        seen = set([(0, 0)])
        ans = []
        
        while k and heap:
            _sum, ind1, ind2 = heappop(heap)
            ans.append([nums1[ind1], nums2[ind2]])
            
            next1 = (ind1 + 1, ind2)
            next2 = (ind1, ind2 + 1)
            
            if next1[0] < len1 and next1 not in seen:
                heappush(heap, (nums1[next1[0]] + nums2[next1[1]], *next1))
                seen.add(next1)
                
            if next2[1] < len2 and next2 not in seen:
                heappush(heap, (nums1[next2[0]] + nums2[next2[1]], *next2))
                seen.add(next2)
            
            k -= 1
        
        return ans
        