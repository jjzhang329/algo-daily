# using hash  sets to store rows, cols and boxes value 
# boxes value can be seen as (r//3)*3 + c // 3
# for example, r = 0, c = 0 => box 0
# r = 4, c = 5 => box 4

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                if val in rows[r] or val in cols[c]:
                    return False 
                rows[r].add(val)
                cols[c].add(val)

                #check the box
                idx = (r // 3)*3 + c // 3
                if val in boxes[idx]:
                    return False 
                boxes[idx].add(val)
                
        return True
