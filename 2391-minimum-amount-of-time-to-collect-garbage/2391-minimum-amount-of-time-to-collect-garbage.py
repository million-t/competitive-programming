class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        ans = 0
        addit = defaultdict(int)
        
        for indx, house in enumerate(garbage):
            count = Counter(house)
            
            for char, freq in count.items():
                ans += freq + addit[char]
                addit[char] = 0
            
            if indx == len(garbage) - 1:
                continue
                
            for char in 'MPG':
                addit[char] += travel[indx]
        
        return ans
                