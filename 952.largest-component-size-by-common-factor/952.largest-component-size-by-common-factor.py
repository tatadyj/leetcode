#
# @lc app=leetcode id=952 lang=python3
#
# [952] Largest Component Size by Common Factor
#

# @lc code=start
def all_primes(n): # all primes < n
    if n <= 2:
        return []

    # Initialize numbers[0] and numbers[1] as False because 0 and 1 are not prime.
    # Initialze numbers[2] through numbers[n-1] as True because we assume each number
    # is prime until we find a prime number (p) that is a divisor of the number
    numbers = [False, False] + [True] * (n - 2)
    for p in range(2, int(sqrt(n)) + 1):
        if numbers[p]:
            # Set all multiples of p to false because they are not prime.
            for multiple in range(p * p, n, p):
                numbers[multiple] = False

    # numbers[index] will only be true where index is a prime number
    # return the number of indices whose value is true.
    return [i for i,v in enumerate(numbers) if v]

class Union_Find:
    def __init__(self, n):
        self.n = n 
        self.parent = [i for i in range(n)]
        
    def find(self, x):
        if self.parent[x] == x:
            return x 
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        self.parent[y_root] = x_root

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:        
        primes = all_primes( int( sqrt(max(nums) + 1) ) + 1 ) 
        uf = Union_Find(max(nums) + 1)

        for i in range(len(nums)):
            x = nums[i] # copy of nums[i]
            for p in primes:
                if p > x: break 
                if x % p == 0:
                    uf.union(nums[i], p) # not union(x, p)
                    while x % p == 0: x //= p 
            if x > 1:
                uf.union(nums[i], x)

        group_count = defaultdict(int)
        for num in nums:
            group_count[uf.find(num)] += 1

        return max(group_count.values())

        
# @lc code=end

