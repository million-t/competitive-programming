class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        countDict = {}
        for num in arr:
            if num in countDict.keys():
                countDict[num] += 1
            else:
                countDict[num] = 1
        countValList = sorted(list(countDict.values()))
        output = 0
        numOfRemovedNums = 0
        while numOfRemovedNums<len(arr)//2:
            numOfRemovedNums += countValList.pop()
            output += 1
        return output
