from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        queue, ans = [], []
        for num in changed:
            if queue and 2*queue[0] == num:
                ans.append(queue.pop(0))
            else:
                queue.append(num)
        return ans if not queue else []
 
