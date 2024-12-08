#
# @lc app=leetcode id=698 lang=python3
#
# [698] Partition to K Equal Sum Subsets
#

# @lc code=start
def loop_over_nums(): # 固定盒子， 把哪个球放入盒子
        nums.sort()
        total = sum(nums)
        if total % k != 0:
            return False 

        n = len(nums)
        visited = [False] * n

        def dfs(start, count, sum):
            if count == k:
                return True 

            if sum > total / k:
                return False 

            if sum == total / k:
                return dfs(0, count+1, 0)

            for i in range(start, n):
                if not visited[i]:
                    if i-1 >= start and nums[i] == nums[i-1] and not visited[i-1]:
                        continue
                    visited[i] = True 
                    if dfs(i+1, count, sum+nums[i]):
                        return True 
                    visited[i] = False 
            return False 


        return dfs(0, 0, 0)

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        '''
        TLE
        '''
        nums.sort(reverse=True)
        total = sum(nums)
        if total % k != 0:
            return False 

        n = len(nums)
        bucket = [0] * k 
        def dfs(i): # 固定球， 把球放入哪个盒子
            if i == len(nums):
                for i in range(len(bucket)):
                    if bucket[i] != total / k:
                        return False
                return True
            
            for b in range(k):
                if bucket[b] + nums[i] > total / k: continue
                bucket[b] += nums[i]
                if dfs(i+1):
                    return True
                bucket[b] -= nums[i]
            return False

        return dfs(0)
    
# @lc code=end

