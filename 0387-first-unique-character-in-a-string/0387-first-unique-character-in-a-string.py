class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        
        count = defaultdict(list)
        
        for i, char in enumerate(s):
            count[char].append(i)
        
        for val in count.values():
            if len(val) == 1:
                return val[0]
        
        return -1
        