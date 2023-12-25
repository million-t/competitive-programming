class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        
        for row in range(len(box)):
            
            right = len(box[0]) - 1
            for left in range(len(box[0]) - 1, -1, -1):
                if box[row][left] == '*':
                    right = left - 1
                    
                elif box[row][left] == '#':
                    box[row][right], box[row][left] = box[row][left], box[row][right]
                    right -= 1
        
        ans = []
        for col in range(len(box[0])):
            col_val = []
            for row in range(len(box)):
                col_val.append(box[row][col])
            
            ans.append(col_val[::-1])
        
        return ans
                    
                    
        