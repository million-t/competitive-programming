class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-1-i], s[i]
            
        '''
        l, r = 0, len(s) - 1
        while l<r:
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
        '''
        