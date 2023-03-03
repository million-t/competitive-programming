class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def f(s):
            return s.count(sorted(s)[0])
        
        
        for i in range(len(words)):
            words[i] = f(words[i])
        
        words.sort()
        size = len(words)
        
        ans = []
        for query in queries:
            
            frequency_of_least = f(query)
            ans.append(size - bisect_right(words, frequency_of_least))
        
        return ans
            
        