class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        loses = defaultdict(int)
        for w, l in matches:
            loses[w]
            loses[l] += 1
        
        ans = [[], []]
        for player in sorted(loses):
            if loses[player] < 2:
                ans[loses[player] > 0].append(player)
        
        return ans
        