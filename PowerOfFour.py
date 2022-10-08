class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def isPow(num):
            if num %4 and num!= 1:
                return False
            elif num < 4:
                if num ==1: return True
                else: return False
            else:
                return isPow(num/4)
        return isPow(abs(n)) if n>=0 else False
