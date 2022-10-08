class Solution:
    def myPow(self, x: float, n: int) -> float:
        def raisedTo(base,power):
            if power in [0,1]:
                return 1 if power==0 else base
            else:
                temp = raisedTo(x,power//2)
                result = base*temp*temp if power%2 else temp*temp
                return result
        return raisedTo(x,abs(n)) if n>=0 else 1/(raisedTo(x,abs(n)))
                
