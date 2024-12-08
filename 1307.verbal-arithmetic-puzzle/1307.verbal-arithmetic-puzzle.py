#
# @lc app=leetcode id=1307 lang=python3
#
# [1307] Verbal Arithmetic Puzzle
#

# @lc code=start
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        words = [word[::-1] for word in words]
        for word in words:
            if len(word) > len(result):
                return False
        result = result[::-1]

        map = [-1] * 26 
        visited = [False] * 10

        def dfs(i, j, total): # row, col, sum
            if j == len(result): # final edge case
                if total != 0:
                    return False 
                if len(result) > 1 and map[ord(result[-1]) - ord('A')] == 0: 
                    # leading zeros, 0 is ok, 00 is not ok
                    return False 
                return True 


            if i == len(words): # edge case where jth column is done
                ch = ord(result[j]) - ord('A')
                if map[ch] != -1:
                    if total%10 != map[ch]:
                        return False 
                    else:
                        # dfs next column
                        return dfs(0, j+1, total//10)
                else:
                    if visited[total%10]:
                        return False 
                    else:
                        map[ch] = total%10 
                        visited[total%10] = True 
                        if dfs(0, j+1, total//10):
                            return True
                        map[ch] = -1
                        visited[total%10] = False 
                        return False

            if j >= len(words[i]) : # edge case of missing char. e.g. [AAA, BB]
                return dfs(i+1, j, total)

            char = ord(words[i][j]) - ord('A')
            if map[char] != -1:
                if len(words[i]) > 1 and j == len(words[i])-1 and map[char] == 0:
                    return False
                return dfs(i+1, j, total+map[char])
            else:
                for k in range(10):
                    if visited[k]: continue
                    if k == 0 and len(words[i]) > 1 and j == len(words[i])-1:
                        # leading zeros
                        continue 
                    map[char] = k
                    visited[k] = True
                    if dfs(i+1, j, total+k):
                        return True 
                    map[char] = -1
                    visited[k] = False
                return False

        res = dfs(0, 0, 0)
        #print(map)
        return res
           
# @lc code=end

