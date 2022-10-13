class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = sorted([[p,s] for p,s in zip(position,speed)],reverse = True)
        stack = []
        for pos,s in arr:
            time = (target-pos)/s
            stack.append(time)
            if len(stack)>1 and stack[-1]<=stack[-2]:
                stack.pop()

        return len(stack)
