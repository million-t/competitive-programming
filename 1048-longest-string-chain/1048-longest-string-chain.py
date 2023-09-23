class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        
        
        words.sort(key = lambda x: len(x))
        visited = defaultdict(int)
        ans = 0
        
        for word in words:
            
            cur_ans = 1
            pre = [char for char in word]
            post = []
            
            while pre:
                temp = pre.pop()
                prev = ''.join(pre + post[::-1])
                cur_ans = max(cur_ans, visited[prev] + 1)
                post.append(temp)
                
            ans = max(ans, cur_ans)
            visited[word] = cur_ans
                
        return ans
                
        
        
        