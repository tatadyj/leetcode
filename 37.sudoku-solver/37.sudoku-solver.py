#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
def is_valid(board, row, col, val):
    for j in range(len(board[0])):
        if board[row][j] == str(val):
            return False 

    for i in range(len(board)):
        if board[i][col] == str(val):
            return False 

    start_row = (row // 3) * 3 
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == str(val):
                return False 
    return True

def bt(board):
    # 若有解，返回True；若无解，返回False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                for k in range(1, 10):
                    if is_valid(board, i, j, k):
                        board[i][j] = str(k)
                        ret = bt(board)
                        if ret: 
                            return True 
                        board[i][j] = "."
                # 若数字1-9都不能成功填入空格，返回False无解
                return False
    return True 


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        bt(board)
        
# @lc code=end

