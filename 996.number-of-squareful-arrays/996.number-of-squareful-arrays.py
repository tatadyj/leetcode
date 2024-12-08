#
# @lc app=leetcode id=996 lang=python3
#
# [996] Number of Squareful Arrays
#

# @lc code=start
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        visited = [False] * n
        adj_dict = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if math.sqrt(nums[i] + nums[j]) == int(math.sqrt(nums[i] + nums[j])):
                    adj_dict[i].append(j)

        def dfs(curr, count):
            nonlocal res
            if count == n:
                res += 1
                return 

            for j,nxt in enumerate(adj_dict[curr]):
                if not visited[nxt]:
                    # 同一层 e.g. [2, 2, 2] 只取第一个2 
                    if j-1 >= 0 and nums[nxt] == nums[adj_dict[curr][j-1]] and not visited[adj_dict[curr][j-1]]:
                        continue
                    visited[nxt] = True 
                    dfs(nxt, count+1)
                    visited[nxt] = False 


        res = 0        
        for i in range(n):
            # 在同一层 e.g.[2, 2, 2], 只取第一个2 
            if i-1 >= 0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue
            visited[i] = True 
            dfs(i, 1)
            visited[i] = False 
        return res     
# @lc code=end

