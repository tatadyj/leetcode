#
# @lc app=leetcode id=2953 lang=python3
#
# [2953] Count Complete Substrings
#

# @lc code=start
class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        def is_ok(freq):
            for key in freq:
                if freq[key] != k:
                    return False 
            return True

        def get_count(w):
            count = 0
            nunique = len(set(w))
            for L in range(1, nunique+1):
                # window size = L*k
                freq = defaultdict(int)
                for r in range(len(w)):
                    freq[w[r]] += 1
                    # exclude end
                    if r-L*k >= 0:
                        freq[w[r-L*k]] -= 1
                        if freq[w[r-L*k]] == 0:
                            freq.pop(w[r-L*k])
                    # count 
                    if r+1-L*k >= 0:
                        if is_ok(freq):
                            count += 1
            #print(w, L, count)
            return count

        res = 0
        i = 0
        while i < n:
            j = i + 1
            while j < n and abs(ord(word[j]) - ord(word[j-1])) <= 2:
                j += 1
            res += get_count(word[i:j])
            i = j 
        return res   
# @lc code=end

