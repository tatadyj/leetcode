#
# @lc app=leetcode id=773 lang=python3
#
# [773] Sliding Puzzle
#

# @lc code=start
from typing import List 
from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        nrows, ncols = len(board), len(board[0])
        s = ''
        for i in range(nrows):
            for j in range(ncols):
                s += str(board[i][j])

        goal_str = '123450'

        queue = deque()
        visited = set()
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        queue.append(s)
        visited.add(s)
        
        step = 0 
        while queue:

            size = len(queue)
            for _ in range(size):
                curr_str = queue.popleft()
                if curr_str == goal_str:
                    return step 

                # get '0'
                idx = curr_str.index('0')
                row_idx = idx // ncols
                col_idx = idx % ncols 

                for dir in dirs:
                    delta_row, delta_col = dir 
                    new_row_idx = row_idx + delta_row 
                    new_col_idx = col_idx + delta_col 

                    if 0 <= new_row_idx <= nrows - 1 and 0 <= new_col_idx <= ncols - 1:
                        new_idx = new_row_idx * ncols + new_col_idx 
                        curr = list(curr_str)
                        curr[idx], curr[new_idx] = curr[new_idx], curr[idx]
                        temp_str = ''.join(curr)

                        if  temp_str not in visited:
                            queue.append(temp_str)
                            visited.add(temp_str)
            step += 1

        return -1 
        
#print(Solution().slidingPuzzle([[4,1,2],[5,0,3]]))
# @lc code=end

