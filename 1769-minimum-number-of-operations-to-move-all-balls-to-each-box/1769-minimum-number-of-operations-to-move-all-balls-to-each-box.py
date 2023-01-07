class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        size = len(boxes)
        num_operations = [0]*size
        
        for position in range(size):
        
            for indx, num in enumerate(boxes):
                if num == '1':
                    num_operations[position] += abs(position - indx)
        
        return num_operations