#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
def bt(letter_map, ans, path, digits, index):
    if len(path) == len(digits):
        ans.append("".join(path))
        return 
    
    for letter in letter_map[digits[index]]:
        path.append(letter)
        bt(letter_map, ans, path, digits, index+1)
        path.pop()

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return [] 
            
        letter_map = {
            "2": "abc",  # 2
            "3": "def",  # 3
            "4": "ghi",  # 4
            "5": "jkl",  # 5
            "6": "mno",  # 6
            "7": "pqrs", # 7
            "8": "tuv",  # 8
            "9": "wxyz"  # 9
        }
        ans, path = [], []
        bt(letter_map, ans, path, digits, 0)
        return ans        
# @lc code=end

