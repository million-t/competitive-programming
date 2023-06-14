class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(image), len(image[0])
        
        
        for row in range(rows):
            for col in range(cols//2):
                image[row][col], image[row][cols - col - 1] = image[row][cols - col - 1], image[row][col]
                
        
        
        for row in range(rows):
            for col in range(cols):
                image[row][col] = 1 - image[row][col]
        
        return image
        