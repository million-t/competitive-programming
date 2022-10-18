class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix, a = [], 0
        for num in arr:
            a = a^num
            prefix.append(a)
        output = []
        for x, y in queries:
            if x:
                output.append(prefix[y]^prefix[x-1])
            else:
                output.append(prefix[y])
        return output
