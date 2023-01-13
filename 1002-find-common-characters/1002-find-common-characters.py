class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        size = len(words)
        arr = [101]*26
        offset = 97
        
        for word in words:
            count = [0]*26
            for char in word:
                index = ord(char) - offset
                count[index] += 1
            
            for i, c in enumerate(count):
                arr[i] = min(arr[i], c)
        common = []
        for indx, val in enumerate(arr):
            i = val
            while i!= 0 and i!= 101:
                common.append(chr(indx + offset))
                i -= 1
        return common
        