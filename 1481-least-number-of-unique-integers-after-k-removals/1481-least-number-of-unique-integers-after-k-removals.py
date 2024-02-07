class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        temp = sorted([(freq, num) for num, freq in Counter(arr).items()])
        pref = 0
        
        for indx, (freq, num) in enumerate(temp):
            if freq > k:
                return len(temp) - indx
            
            elif freq == k:
                return len(temp) - indx - 1
            
            k -= freq
        
        return 0