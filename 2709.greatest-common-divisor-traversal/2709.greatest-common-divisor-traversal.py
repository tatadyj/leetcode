#
# @lc app=leetcode id=2709 lang=python3
#
# [2709] Greatest Common Divisor Traversal
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
        if x_root > y_root:
            x_root, y_root = y_root, x_root
        self.parent[y_root] = x_root

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        max_num = max(nums) + 1 # + 1 due to the all_primes func
        primes = all_primes(max_num)
        
        v2i = defaultdict(int)
        for i,p in enumerate(primes):
            v2i[p] = i 

        n = len(nums)
        m = len(primes)
        uf = Union_Find(n+m)
        for i in range(n):
            x = nums[i]
            for j in range(m):
                p = primes[j]
                if x < p: break 
                if p*p > x:
                    uf.union(i, v2i[x]+n)
                    break
                    
                if x % p == 0:
                    uf.union(i, j+n)
                    while x % p == 0: x //= p
            

        for i in range(1, n):
            if uf.find(i) != uf.find(0):
                return False 
        return True 
         
# @lc code=end

