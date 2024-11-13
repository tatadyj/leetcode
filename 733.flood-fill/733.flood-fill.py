#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(r, c):
            for dr, dc in dir:
                nxt_r, nxt_c = r + dr, c + dc 
                if nxt_r < 0 or nxt_r >= m or nxt_c < 0 or nxt_c >= n: continue 
                if image[nxt_r][nxt_c] == color: continue
                if image[nxt_r][nxt_c] == orig:
                    image[nxt_r][nxt_c] = color
                    dfs(nxt_r, nxt_c)

        orig = image[sr][sc]
        image[sr][sc] = color 
        dfs(sr, sc)
        return image   
# @lc code=end

