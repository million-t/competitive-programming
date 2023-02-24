class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        size = len(position)
        
        for i in range(size):
            position[i] = [position[i], speed[i]]
        
        position.sort()
        
        stack = []
        for x, v in position:
            
            time = (target - x)/v
            while stack and time >= stack[-1]:
                stack.pop()
            
            stack.append(time)
        
        return len(stack)