#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
def is_valid(board, row, col):
    for i in range(row):
        if board[i][col] == "Q":
            return False 
    
    i, j = row-1, col+1
    while i >= 0 and j < len(board[0]):
        if board[i][j] == "Q":
            return False 
        i -= 1 
        j += 1

    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False 
        i -= 1
        j -= 1

    return True 

def bt(ans, board, n, row):
    if row == n:
        ans.append([''.join(row) for row in board])
        return 

    for col in range(n):
        if is_valid(board, row, col):
            board[row][col] = "Q"
            bt(ans, board, n, row+1)
            board[row][col] = "."


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.']*n for i in range(n)]
        bt(ans, board, n, 0)
        return ans   
# @lc code=end

