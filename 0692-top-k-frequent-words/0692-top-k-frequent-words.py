class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        heap = []
        counts = Counter(words)
        
        for word, count in counts.items():
            heapq.heappush(heap, (-1*count, word))
            
        
        res = []
        while k:
            freq, word = heapq.heappop(heap)
            res.append(word)
            k -= 1
        
        return res