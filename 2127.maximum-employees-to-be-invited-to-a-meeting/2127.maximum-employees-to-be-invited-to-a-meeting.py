#
# @lc app=leetcode id=2127 lang=python3
#
# [2127] Maximum Employees to Be Invited to a Meeting
#

# @lc code=start
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)

        in_degree = [0] * n
        depth = [1] * n
        for i,v in enumerate(favorite):
            in_degree[v] += 1

        visited = [False] * n
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i) 
                visited[i] = True        
        
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                visited[curr] = True
                nxt = favorite[curr]
                depth[nxt] = depth[curr] + 1
                in_degree[nxt] -= 1 
                if in_degree[nxt] == 0:
                    queue.append(nxt)

        max_cycle = 0
        max_link = 0
        for i in range(n):
            if visited[i]: continue 
            j = i 
            count = 0 
            while not visited[j]:
                count += 1
                visited[j] = True 
                j = favorite[j]
            if count >= 3:
                max_cycle = max(max_cycle, count)
            if count == 2:
                max_link +=  depth[i] + depth[favorite[i]]
        return max(max_cycle, max_link)


# @lc code=end

