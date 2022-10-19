class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        l = 0
        output = 0
        for r in range(len(s)):
            if s[r] not in count.keys():
                count[s[r]] = 1
            else:
                count[s[r]] += 1
            if count[s[r]]>1:
                while s[l]!=s[r]:
                    count.pop(s[l])
                    l+=1
                count[s[l]]-=1
                l+=1
            output = max(output, r - l + 1)
        return output
