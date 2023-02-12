class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        count = Counter(ransomNote)
        for char in magazine:
            
            if char in count:
                count[char] -= 1
                
                if count[char] == 0:
                    count.pop(char)
        return count == {}    
        
