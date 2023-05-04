class Solution:
    def racecar(self, target: int) -> int:
        
        
        def accelerate(pos, speed):
            pos += speed
            speed *= 2
            return pos, speed
        
        def decelerate(pos, speed):
            speed = 1 if speed < 0 else -1
            return pos, speed
        
        
        queue = deque([(0, 1)])
        visited = set([(0, 1)])
        steps = 0

        
        while queue:
            
            size = len(queue)
            for _ in range(size):
                pos, speed = queue.popleft()
                
                if pos == target:
                    return steps 
                
                acc = accelerate(pos, speed)
                if acc not in visited:
                    queue.append(acc)
                    
                if (pos + speed > target and speed > 0) or (pos + speed < target and speed < 0):
                    dec = decelerate(pos, speed)        
                    
                    if dec not in visited:
                        queue.append(dec)

            steps += 1
            
            
            
        