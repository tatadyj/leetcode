#
# @lc app=leetcode id=1577 lang=python3
#
# [1577] Number of Ways Where Square of Number Is Equal to Product of Two Numbers
#

# @lc code=start

def hashmap_method(self, nums1: List[int], nums2: List[int]) -> int:
    def count_triplets(nums1, nums2):
        count = 0
        for x in nums1:
            map = defaultdict(int)
            for y in nums2:
                if x*x % y == 0:
                    count += map[x*x // y]
                map[y] += 1
        return count 

    return count_triplets(nums1, nums2) + count_triplets(nums2, nums1)

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        def count_triplets(nums1, nums2):
            count = 0 
            for x in nums1:
                i = 0 
                j = len(nums2) - 1
                while i < j:
                    #print(x, i, j, count)
                    if x*x > nums2[i] * nums2[j]:
                        i += 1
                    elif x*x < nums2[i] * nums2[j]:
                        j -= 1
                    else:
                        if nums2[i] != nums2[j]:
                            p = i 
                            while p < j and nums2[p] == nums2[i]:
                                p += 1
                            q = j 
                            while q > i and nums2[q] == nums2[j]:
                                q -= 1
                            count += (p - i) * (j - q)
                            i = p
                            j = q
                        else:
                            L = j - i + 1
                            count += L * (L - 1) // 2
                            break
            return count 
        return count_triplets(nums1, nums2) + count_triplets(nums2, nums1)
    
# @lc code=end

