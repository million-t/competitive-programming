class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        
        
        pref = [stones[0]]
        for indx in range(1, len(stones)):
            pref.append(pref[-1] + stones[indx])
        
        alice = [0]*len(pref)
        bob = [0]*len(pref)
        alice[-1] = pref[-1]
        bob[-1] = -pref[-1]
        
        for indx in range(len(pref) - 2, 0, -1):
            alice[indx] = max(alice[indx + 1], bob[indx + 1] + pref[indx])
            bob[indx] = min(bob[indx + 1], alice[indx + 1] - pref[indx])
        
        
        return alice[1]
            