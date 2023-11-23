class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose = {}
        for win, loss in matches:
            lose[win] = lose.get(win, 0)
            lose[loss] = lose.get(loss, 0) + 1
        ans = [[],[]]
        for key, val in sorted(lose.items()):
            if val == 0:
                ans[0].append(key)
            elif val == 1:
                ans[1].append(key)
        return ans
