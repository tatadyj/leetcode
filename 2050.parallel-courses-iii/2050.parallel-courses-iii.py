#
# @lc app=leetcode id=2050 lang=python3
#
# [2050] Parallel Courses III
#

# @lc code=start
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj_dict = defaultdict(list)
        in_degree = [0] * n
        for a,b in relations:
            adj_dict[a-1].append(b-1)
            in_degree[b-1] += 1

        t = [0] * n # min number of month when it finishes
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
                t[i] = time[i]

        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()              
                for nxt in adj_dict[curr]:
                    in_degree[nxt] -= 1
                    t[nxt] = max(t[nxt], t[curr] + time[nxt])
                    if in_degree[nxt] == 0:
                        queue.append(nxt)
                #print(queue, time)
        return max(t)
        

# @lc code=end

