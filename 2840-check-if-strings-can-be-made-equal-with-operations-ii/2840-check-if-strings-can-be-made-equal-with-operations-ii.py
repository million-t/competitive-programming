class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even = sorted([s1[indx] for indx in range(0, len(s1), 2)]) == sorted([s2[indx] for indx in range(0, len(s2), 2)])
        odd = sorted([s1[indx] for indx in range(1, len(s1), 2)]) == sorted([s2[indx] for indx in range(1, len(s2), 2)])
        return odd and even