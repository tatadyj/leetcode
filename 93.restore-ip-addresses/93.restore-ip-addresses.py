#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start

def isValid(s):
    if s[0] == '0' and len(s) > 1: 
        return False
    if int(s) < 0 or int(s) > 255: 
        return False
    return True


def bt(ans, ip, s):

    if len(ip) == 4:
        if len(s) == 0:
            ans.append(ip[:])
        return 

    for i in range(len(s)):
        if isValid(s[0:i+1]):
            ip.append(s[0:i+1])
        else:
            continue
        
        bt(ans, ip, s[i+1:])
        ip.pop()


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans, ip = [], []
        if (len(s) > 12): return ans
        bt(ans, ip, s)
        return ['.'.join(ip) for ip in ans]
        
# @lc code=end

