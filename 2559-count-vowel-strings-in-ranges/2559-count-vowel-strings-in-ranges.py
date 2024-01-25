class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowels = set("AaEeIiOoUu")
        pref = [0]*(len(words) + 1)
        for indx, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                pref[indx] = 1
        
        for indx in range(1, len(words)):
            pref[indx] += pref[indx - 1]
        
        ans = []
        for l, r in queries:
            ans.append(pref[r] - pref[l - 1])
        
        return ans