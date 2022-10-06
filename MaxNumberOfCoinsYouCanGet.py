class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        myCoins = 0
        while piles:
            piles.pop()
            myCoins += piles.pop()
            piles.pop(0)
        return myCoins
