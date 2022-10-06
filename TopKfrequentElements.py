class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tempDict = {}
        for num in nums:
            if num in tempDict.keys():
                tempDict[num][0]+=1
            else:
                tempDict[num] = [1,num]
        frequencyList = sorted(list(tempDict.values()))
        output = []
        for i in range(k):
            output.append(frequencyList.pop()[1])
        return output
        
