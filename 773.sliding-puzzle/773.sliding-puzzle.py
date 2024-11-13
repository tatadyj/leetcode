#
# @lc app=leetcode id=773 lang=python3
#
# [773] Sliding Puzzle
#

# @lc code=start
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target_state = '123450'
        init_state = ''.join([str(b) for b in board[0]]) + ''.join([str(b) for b in board[1]])
        if init_state == target_state:
            return 0
        queue = deque()
        queue.append((init_state, 0))
        visited = set(init_state)
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def swap(string, i, j):
            s = list(string)
            s[i], s[j] = s[j], s[i]
            return ''.join(s)

        while queue:
            size = len(queue)
            for _ in range(size):
                curr_state, level = queue.popleft()
                for dx, dy in dir:
                    idx = curr_state.index('0')
                    x, y = idx // 3, idx % 3
                    nxt_x, nxt_y = x + dx, y + dy 
                    if nxt_x < 0 or nxt_x >= 2 or nxt_y < 0 or nxt_y >= 3: continue 
                    nxt_idx = nxt_x * 3 + nxt_y
                    nxt_state = swap(curr_state, idx, nxt_idx)
                    if nxt_state in visited: continue 
                    if nxt_state == target_state:
                        return level + 1 
                    queue.append((nxt_state, level+1))
                    visited.add(nxt_state)
        return -1

        
#print(Solution().slidingPuzzle([[4,1,2],[5,0,3]]))
# @lc code=end

