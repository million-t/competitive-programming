class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = defaultdict(list)
        
        for word in strs:
            seen[''.join(sorted(word))].append(word)
        
        ans_arr = []
        for val in seen.values():
            ans_arr.append(val)
        
        return ans_arr
        