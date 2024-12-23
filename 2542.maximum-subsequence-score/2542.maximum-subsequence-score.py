#
# @lc app=leetcode id=2542 lang=python3
#
# [2542] Maximum Subsequence Score
#

# @lc code=start
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        arr = []
        for n1, n2 in zip(nums1, nums2):
            arr.append((n2, n1))

        arr.sort(reverse=True)

        res = 0
        sum = 0
        pq = [] # min heap
        for i in range(len(arr)):
            min_val = arr[i][0]
            heapq.heappush(pq, arr[i][1])
            sum += arr[i][1]

            if len(pq) > k:
                top = heapq.heappop(pq)
                sum -= top

            if len(pq) == k:
                res = max(res, min_val * sum)
        return res    
# @lc code=end

