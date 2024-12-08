#
# @lc app=leetcode id=1723 lang=python3
#
# [1723] Find Minimum Time to Finish All Jobs
#

# @lc code=start
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        jobs.sort(reverse=True)
        workers = [0] * k

        def dfs(curr, limit):
            if curr == n:
                return True 

            flag = 0
            for i in range(k):
                if workers[i] + jobs[curr] > limit:
                    continue 
                    
                if workers[i] == 0:
                    if flag == 1: continue 
                    flag = 1

                workers[i] += jobs[curr]
                if dfs(curr+1, limit):
                    return True
                workers[i] -= jobs[curr]
            return False 

        left = max(jobs)
        right = sum(jobs)
        while left < right:
            for i in range(k):
                workers[i] = 0
            mid = (left + right) // 2
            if dfs(0, mid):
                right = mid
            else:
                left = mid + 1
        return left



# @lc code=end

