class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp = strs[0]
        r = len(temp)
        for word in strs:
            if r>len(word):
                r = len(word)
            while temp[:r] != word[:r]:
                r-=1
        return temp[:r]
