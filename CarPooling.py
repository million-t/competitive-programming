class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ln = 0
        for x,y,z in trips:
            ln = max(ln, z)
        prefix = [0]*(ln+1)
        for x, y, z in trips:
            prefix[y] += x
            prefix[z] -= x
        p = 0
        for i in range(ln):
            p += prefix[i]
            prefix[i] = p
            if prefix[i]>capacity: 
                return False
        return True
         
        






