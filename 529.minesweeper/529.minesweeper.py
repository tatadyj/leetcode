#
# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#

# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0])

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board 

        queue = deque()
        queue.append(click)
        visited = [[False] * n for _ in range(m)]
        visited[click[0]][click[1]] = True 

        while queue:
            r, c = queue.popleft()
            count = 0
            next = []
            for dr, dc in dir:
                nxt_r, nxt_c = r + dr, c + dc 
                if nxt_r < 0 or nxt_r >= m or nxt_c < 0 or nxt_c >= n: continue
                if visited[nxt_r][nxt_c]: continue 
                if board[nxt_r][nxt_c] == 'M':
                    #visited[nxt_r][nxt_c] = True
                    count += 1
                else:
                    next.append((nxt_r, nxt_c))

            if count == 0:
                board[r][c] = 'B'
                for nxt_r, nxt_c in next:
                    queue.append((nxt_r, nxt_c))
                    visited[nxt_r][nxt_c] = True
            else:
                board[r][c] = str(count)
        return board
# @lc code=end

