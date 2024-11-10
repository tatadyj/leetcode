#
# @lc app=leetcode id=2440 lang=python3
#
# [2440] Create Components With Same Value
#

# @lc code=start
class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        adj_dict = defaultdict(list)
        degree = [0] * n
        for a, b in edges:
            adj_dict[a].append(b)
            adj_dict[b].append(a)
            degree[a] += 1
            degree[b] += 1

        total = sum(nums)
        factors = []
        for s in range(min(nums), int(sqrt(total)) + 1):
            if total % s == 0:
                factors.append(s)
                factors.append(total//s)
        factors.sort()
        
        def topo_sort(s, degree, nums):
            count = 0
            queue = deque()
            for i in range(n):
                if degree[i] == 1:
                    queue.append(i)
            
            while queue:
                curr = queue.popleft()
                if nums[curr] > s:
                    return False
                if nums[curr] == s:
                    count += 1
                for nxt in adj_dict[curr]:
                    degree[nxt] -= 1
                    if nums[curr] < s:
                        nums[nxt] += nums[curr]
                    if degree[nxt] == 1:
                        queue.append(nxt)
            
            return count == total // s
              
        for s in factors:
            if topo_sort(s, degree.copy(), nums.copy()):
                return total // s - 1
        return 0
          

             
# @lc code=end

