class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        pathDict = defaultdict(list)
        for path in paths:
            pathArr = path.split(' ')
            for i in range(1,len(pathArr)):
                curFile = pathArr[i][:-1].split('(')
                pathDict[curFile[1]].append(pathArr[0] + '/' + curFile[0])
        return [val for val in pathDict.values() if len(val)>1]
        