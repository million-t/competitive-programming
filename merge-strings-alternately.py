class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        a = b = 0
        i = 0
        while a<len(word1) and b<len(word2):
            if i%2:
                ans+=word2[b]
                b+=1
            else:
                ans+=word1[a]
                a+=1
            i += 1
        if a<len(word1):
            ans+= word1[a:]
            a+=1
        if b<len(word2):
            ans+= word2[b:]
            b+=1
        return ans
