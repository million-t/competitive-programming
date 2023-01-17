class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        pointer = 0
        
        while pointer < len(arr) - 1 and arr[pointer + 1] > arr[pointer]:
            pointer += 1
        
        if pointer == len(arr) - 1 or pointer == 0:
            return False
        
        while pointer < len(arr) - 1 and arr[pointer + 1] < arr[pointer]:
            pointer += 1
        
        return pointer == len(arr) - 1
        
            
        