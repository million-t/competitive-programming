#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        
        current = i
        greatest = current
        left = current*2 + 1
        right = current*2 + 2
    
        while True:
            if left < n and arr[left] > arr[greatest]:
                greatest = left
                
            if right < n and arr[right] > arr[greatest]:
                greatest = right
            
            if greatest == current:
                break
            
            arr[greatest], arr[current] = arr[current], arr[greatest]
            left = greatest*2 + 1
            right = greatest*2 + 2
            current = greatest
            
        
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        pass
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        
        for i in range(n//2 - 1, -1, -1):
            self.heapify(arr, n, i)
        for i in range(n - 1, -1, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
