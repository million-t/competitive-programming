class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        
        
        usage = defaultdict(set)
        for _id, time in logs:
            usage[_id].add(time)
        
        ans = [0]*k
        for _id in usage:
            ans[len(usage[_id]) - 1] += 1
        
        return ans
        
        
        