
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = list(range(1,n+1))
        i = 0
        while len(arr) > 1:
            i = (i + k - 1)%len(arr)
            arr.pop(i)
            
        return arr[0]