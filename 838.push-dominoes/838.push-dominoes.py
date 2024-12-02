#
# @lc app=leetcode id=838 lang=python3
#
# [838] Push Dominoes
#

# @lc code=start
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        queue = deque()
        rets = [-2] * n

        for i in range(len(dominoes)):
            if dominoes[i] == 'L':
                queue.append((i, -1))
                rets[i] = -1               
            elif dominoes[i] == 'R':
                queue.append((i, 1))            
                rets[i] = 1

        while queue:
            size = len(queue)
            map = defaultdict(int)
            for _ in range(size):
                pos, dir = queue.popleft()
                if dir == 1 and pos+1 < n and rets[pos+1] == -2:
                    map[pos+1] += 1
                if dir == -1 and pos-1 >= 0 and rets[pos-1] == -2:
                    map[pos-1] -= 1
            
            for pos,dir in map.items():
                queue.append((pos, dir))
                rets[pos] = dir
        
        ans = []
        for i in range(n):
            if rets[i] == 1:
                ans.append('R')
            elif rets[i] == -1:
                ans.append('L')
            else:
                ans.append('.')
        return ''.join(ans)
# @lc code=end

