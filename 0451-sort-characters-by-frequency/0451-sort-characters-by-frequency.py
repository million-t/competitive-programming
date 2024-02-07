class Solution:
    def frequencySort(self, s: str) -> str:
        
        count = Counter(s)
        heap = [ (freq, char) for char, freq in count.items()]
        heapify(heap)
        
        res = []
        
        while heap:
            freq, char = heappop(heap)
            
            while freq:
                res.append(char)
                freq -= 1
        
        return ''.join(res[::-1])