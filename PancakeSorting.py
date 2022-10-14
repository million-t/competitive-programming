class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(x):
            for i in range(x//2+1):
                arr[i], arr[x-i] = arr[x-i], arr[i]
        ans = []
        for i in range(len(arr)-1,0,-1):
            for j in range(1,i+1):
                if arr[j]== i+1:
                    flip(j)
                    ans.append(j+1)
                    break
            flip(i)
            ans.append(i+1)
        return ans
