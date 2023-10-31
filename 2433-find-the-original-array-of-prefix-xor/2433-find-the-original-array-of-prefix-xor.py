class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        ans = [pref[0]]
        for indx in range(1, len(pref)):
            ans.append(pref[indx - 1] ^ pref[indx])
        
        return ans
        