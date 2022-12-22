class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        count = {}
        ans = 0
        for food in deliciousness:
            for i in range(22):
                diff = (2**i) - food
                if diff in count:
                    ans+=count[diff]
            count[food] = count.get(food, 0) + 1
        return ans%(10**9 + 7)

