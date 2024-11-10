#
# @lc app=leetcode id=1136 lang=python3
#
# [1136] Parallel Courses
#

# @lc code=start
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj_dict = defaultdict(list)
        in_degree = [0] * n
        for a,b in relations:
            adj_dict[a-1].append(b-1)
            in_degree[b-1] += 1

        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        
        num_semester = 0
        while queue:
            num_semester += 1
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                for nxt in adj_dict[curr]:
                    in_degree[nxt] -= 1
                    if in_degree[nxt] ==0:
                        queue.append(nxt)
        total = sum([i != 0 for i in in_degree])
        if total == 0:
            return num_semester 
        else:
            return -1    
# @lc code=end

