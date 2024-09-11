
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = ['.' * n for _ in range(n)]
        # ['....', '....', '....', '....']
        self.backtracking(n, 0, board, result)
        return result 

    def backtracking(self, n, row, board, result):
        if row == n:
            result.append(board[:])
            return 
        
        for col in range(n):
            if self.is_valid(row, col, board):
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                self.backtracking(n, row+1, board, result)
                board[row]= board[row][:col] + '.' + board[row][col+1:]

    
    def is_valid(self, row, col, board):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
    
        i, j = row-1, col-1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False  # 左上方向已经存在皇后，不合法
            i -= 1
            j -= 1
        
        i, j = row-1, col+1
        while i >= 0 and j < len(board):
            if board[i][j] == 'Q':
                return False #右上方有皇后

            i -= 1
            j += 1

        return True