#
# @lc app=leetcode id=638 lang=python3
#
# [638] Shopping Offers
#

# @lc code=start
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        arr = []
        n = len(price)
        for item in special:
            total = 0
            for i in range(n):
                total += price[i]*item[i]
            if item[-1] < total:
                arr.append(item)

        # 6个物品 每个最多买10个(4-bit->[0,15])
        # xxxx xxxx xxxx xxxx xxxx xxxx
      
        memo = {}
        def dfs(state):
            if state == 0:
                return 0

            if state in memo:
                return memo[state]

            ret = 0 
            for i in range(n):
                num_item = (state >> (i*4)) % 16
                ret += num_item * price[i]

            for comb in arr:
                valid_comb = True
                for i in range(n):
                    num_item = (state >> (i*4) ) % 16
                    if num_item < comb[i]:
                        valid_comb = False
                        break 
                if valid_comb:
                    nxt_state = state 
                    for i in range(n):
                        nxt_state -= comb[i] << (i*4)
                    ret = min(ret, comb[-1] + dfs(nxt_state))
            memo[state] = ret
            return ret 

        state = 0
        for i in range(n):
            state += needs[i] << (i*4)
        
        return dfs(state)
        
# @lc code=end

