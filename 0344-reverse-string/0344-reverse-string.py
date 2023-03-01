class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        def reverse_str(left, right):
            #base case
            if left >= right:
                return
            
            s[left], s[right] = s[right], s[left]
            
            reverse_str(left + 1, right - 1)
        
        
        reverse_str(0, len(s) - 1)