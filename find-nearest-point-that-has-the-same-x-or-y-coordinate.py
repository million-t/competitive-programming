class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = -1
        minDist = float('inf')
        for i, p in enumerate(points):
            if x == p[0] or y == p[1]:
                d = abs(x - p[0]) + abs(y - p[1])
                if minDist > d:
                    minDist = d
                    ans = i
        return ans
