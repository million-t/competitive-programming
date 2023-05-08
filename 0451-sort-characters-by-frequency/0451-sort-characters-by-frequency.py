class Solution:
    def frequencySort(self, s: str) -> str:
        
        count = Counter(s)
        heap = []
        
        for char, freq in count.items():
            heappush(heap, (freq, char))
        
        res = []
        
        while heap:
            freq, char = heappop(heap)
            
            while freq:
                res.append(char)
                freq -= 1
        
        return ''.join(res[::-1])