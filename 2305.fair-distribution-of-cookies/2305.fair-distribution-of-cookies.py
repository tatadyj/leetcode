#
# @lc app=leetcode id=2305 lang=python3
#
# [2305] Fair Distribution of Cookies
#

# @lc code=start
def DFS_loop_cookies(self, cookies: List[int], k: int) -> int:
    """
    TLE
    """
    n = len(cookies)
    plan = [0] * k

    def dfs(cur):
        nonlocal ans
        if cur == n:
            ans = min(ans, max(plan))
            return 
            
        for i in range(k):
            plan[i] += cookies[cur]
            dfs(cur+1)
            plan[i] -= cookies[cur]
    ans = inf
    dfs(0)
    return ans
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        cookies.sort(reverse=True)

        def dfs(plan, curr, limit):
            if curr == n:
                return True

            flag = 0
            for i in range(k):
                if plan[i] + cookies[curr] > limit:
                    continue

                # 减枝
                if plan[i] == 0:
                    if flag == 1:
                        continue 
                    flag = 1

                plan[i] += cookies[curr]
                if dfs(plan, curr+1, limit):
                    return True
                plan[i] -= cookies[curr]
            return False 

        def is_valid(limit):
            plan = [0]*k
            return dfs(plan, 0, limit)
        
        left = max(cookies)
        right = sum(cookies)
        while left < right:
            mid = (left + right) // 2
            if is_valid(mid):
                right = mid
            else:
                left = mid + 1 
        return left
# @lc code=end

