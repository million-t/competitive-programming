
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        num = x
        digits = 0
        temp = x
        while temp:
            digits+=1
            temp//=10
        new = 0
        while digits:
            new += (num%10)*(10**(digits-1))
            num //=10
            digits-=1
        return x == new
