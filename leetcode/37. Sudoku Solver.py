# 二维深度遍历，每次回溯选择一行一例，回溯中的for loop用来选1-9数字
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtracking(board)
    
    def backtracking(self, board):       
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    continue
                
                for num in range(1, 10):
                    if self.is_valid(row, col, num, board):
                        board[row][col] = str(num)
                        if self.backtracking(board): return True
                        board[row][col] = '.'

                return False

        return True

    def is_valid(self, row, col, num, board):
        for n in board[row]:
            if n == str(num):
                return False
        
        for i in range(9):
            if board[i][col] == str(num):
                return False

        row = (row // 3) * 3
        col = ( col // 3) * 3

        for r in range(row, row+3):
            for c in range(col, col+3):
                if board[r][c] == str(num):
                    return False
        
        return True