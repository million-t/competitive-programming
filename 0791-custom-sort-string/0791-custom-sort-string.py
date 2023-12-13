class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        
        
        place = defaultdict(lambda :27)
        for indx, char in enumerate(order):
            place[char] = indx
        
        temp = defaultdict(list)
        for char in s:
            temp[place[char]].append(char)
        
        ans = []
        for indx in sorted(temp.keys()):
            for val in temp[indx]:
                ans.append(val)
        
        return "".join(ans)