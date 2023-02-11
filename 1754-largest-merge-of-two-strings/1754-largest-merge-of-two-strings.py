class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        m, n = len(word1), len(word2)
        
        ptr_1 = 0
        ptr_2 = 0
        
        merge = []
        
        while ptr_1 < m and ptr_2 < n:
            
            while ptr_2 < n and ptr_1 < m and word1[ptr_1:]>=word2[ptr_2:]:
                merge.append(word1[ptr_1])
                ptr_1 += 1
            while ptr_1 < m and ptr_2 < n and word1[ptr_1:]<word2[ptr_2:]:
                merge.append(word2[ptr_2])
                ptr_2 += 1
            
        merge.extend(word1[ptr_1:])
        merge.extend(word2[ptr_2:])
        return "".join(merge)
            
            
        
        
        