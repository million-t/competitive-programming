class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        source = '#'.join(source)
        n = len(source)
        left = 0
        right = 0
        
        comment_removed = ''
        inline_cmnt = False
        block_cmnt = False
        opening_asteriks_indx = -1
        
        for indx, char in enumerate(source):
            
            if block_cmnt and indx > 0 and indx - 1 != opening_asteriks_indx and char == '/' and source[indx-1] == '*':
                block_cmnt = False
                
            elif inline_cmnt and char == '#':
                comment_removed += char
                inline_cmnt = False      

            elif not(inline_cmnt or block_cmnt) and indx < n - 1 and char == '/' and source[indx+1] == '/':
                inline_cmnt = True
                
            elif not(block_cmnt or inline_cmnt) and indx < n - 1 and char == '/' and source[indx+1] == '*':
                block_cmnt = True
                opening_asteriks_indx = indx + 1

            elif not(inline_cmnt or block_cmnt):
                comment_removed += char
        
        no_empltyline_removed = comment_removed.split('#')
        ans = [] 
        
        for line in no_empltyline_removed:
            if line != '':
                ans.append(line)
        return ans
                 
            