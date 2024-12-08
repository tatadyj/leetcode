#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
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
        ans[0] += 1
        return 

    for col in range(n):
        if is_valid(board, row, col):
            board[row][col] = "Q"
            bt(ans, board, n, row+1)
            board[row][col] = "."


class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = [0] 
        board = [['.'] * n for _ in range(n)]
        bt(ans, board, n, 0)
        return ans[0]
             
# @lc code=end

