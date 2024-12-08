#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
def is_valid(s):
    if int(s) < 0 or int(s) > 255:
        return False 
    if s[0] == "0" and len(s) > 1:
        return False 

    return True 
            
    

def bt(ans, path, s):
    if len(path) == 4 and len(s) == 0:
        ans.append(".".join(path))
        return 

    for i in range(len(s)):
        if is_valid(s[:i+1]):
            path.append(s[:i+1])
            bt(ans, path, s[i+1:])
            path.pop()



class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12: # 4 integers, 3*4 = 12
            return []
        ans, path = [], []
        bt(ans, path, s)
        return ans 
        
# @lc code=end

