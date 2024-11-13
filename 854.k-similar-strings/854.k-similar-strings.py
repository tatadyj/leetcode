#
# @lc app=leetcode id=854 lang=python3
#
# [854] K-Similar Strings
#

# @lc code=start
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        n = len(s1)
        if s1 == s2:
            return 0
        
        queue = deque()
        queue.append((s1, 0))
        visited = set([s1])

        def swap(string, i, j):
            s = list(string)
            s[i], s[j] = s[j], s[i]
            return ''.join(s)

     
        while queue:
            size = len(queue)
            for _ in range(size):
                curr_s1, level = queue.popleft()
                i = level
                while i < n and curr_s1[i] == s2[i]:
                    i += 1
                for j in range(i+1, n):
                    if curr_s1[j] == s2[i]:
                        nxt_s1 = swap(curr_s1, i, j)
                        if nxt_s1 in visited: continue
                        if nxt_s1 == s2:
                            return level + 1 
                        else:
                            queue.append((nxt_s1, level+1))
                            visited.add(nxt_s1)

          
# @lc code=end

