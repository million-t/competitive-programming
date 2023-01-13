class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def subBox_check(c1, c2, r1, r2):
            seen = set()
            for row in range(r1, r2):
                for col in range(c1, c2):
                    if board[row][col] != '.' and board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
            return True
        def ver_check(m, n):
            for col in range(n):
                seen = set()
                for row in range(m):
                    if board[row][col] != '.' and board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
            return True
        def hor_check(m, n):
            
            for row in range(n):
                seen = set()
                for col in range(m):
                    if board[row][col] != '.' and board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
            return True
        hor_boxes1 = subBox_check(0, 3, 0, 3) and subBox_check(3, 6, 0, 3) and subBox_check(6, 9, 0, 3)
        hor_boxes2 = subBox_check(0, 3, 3, 6) and subBox_check(3, 6, 3, 6) and subBox_check(6, 9, 3, 6)
        hor_boxes3 = subBox_check(0, 3, 6, 9) and subBox_check(3, 6, 6, 9) and subBox_check(6, 9, 6, 9)
        m, n = len(board), len(board[0])
        return hor_boxes1 and hor_boxes2 and hor_boxes3 and hor_check(m,n) and ver_check(m,n)
                    
                