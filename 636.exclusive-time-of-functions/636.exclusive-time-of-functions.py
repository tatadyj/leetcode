#
# @lc app=leetcode id=636 lang=python3
#
# [636] Exclusive Time of Functions
#

# @lc code=start
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = defaultdict(int)
        n = len(logs)
        for i in range(n):
            id, status, time = logs[i].split(':')
            id, time = int(id), int(time)
            if status == 'start':
                stack.append((id, status, time))
            if status == 'end':
                if stack:
                    _, _, prev_time = stack.pop()
                    delta = time - prev_time + 1 
                    res[id] += delta 
                    if stack:
                        prev_id = stack[-1][0]
                        res[prev_id] -= delta
        return [res[k] for k in sorted(res)]        
# @lc code=end

