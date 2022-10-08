class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def isPow(num):
            if num %3 and num!= 1:
                return False
            elif num < 3:
                if num ==1: return True
                else: return False
            else:
                return isPow(num/3)
        return isPow(abs(n)) if n>=0 else False
