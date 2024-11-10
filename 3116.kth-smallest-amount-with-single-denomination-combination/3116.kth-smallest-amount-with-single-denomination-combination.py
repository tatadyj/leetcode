#
# @lc app=leetcode id=3116 lang=python3
#
# [3116] Kth Smallest Amount With Single Denomination Combination
#

# @lc code=start
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        dic = defaultdict(list)
        for i in range(1, n+1):
            for comb in itertools.combinations(coins, i):
                dic[len(comb)].append(math.lcm(*comb))

        def count_less_or_equal(val):
            res = 0 
            for i in range(1, n+1):
                for lcm in dic[i]:
                    res += val // lcm * (-1)**(i+1)
            return res 

        left = 1
        right = 2*10**9*math.prod(coins)
        while left < right:
            mid = (left + right) // 2
            if count_less_or_equal(mid) >= k:
                right = mid 
            else:
                left = mid + 1
        return left
        
# @lc code=end

