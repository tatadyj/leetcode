#
# @lc app=leetcode id=827 lang=python3
#
# [827] Making A Large Island
#

# @lc code=start
def dfs(grid, m, n, i, j, num_island):
    if i < 0 or j < 0 or i >= m or j >=n or grid[i][j] == 0 or grid[i][j] != 1:
        return 0 

    grid[i][j] = num_island
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    area = 1
    for direction in directions:
        next_i, next_j = i + direction[0], j + direction[1]
        area += dfs(grid, m, n, next_i, next_j, num_island)
    return area 

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        island_map = {}
        m, n = len(grid), len(grid[0])
        num_island = 1 # start with 2
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num_island += 1
                    area = dfs(grid, m, n, i, j, num_island)
                    island_map[num_island] = area 
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_area = max(island_map.values()) if island_map else 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    connect_area = 1
                    seen_island = set()
                    for direct in directions:
                        next_i, next_j = i + direct[0], j + direct[1]
                        if next_i < 0 or next_j < 0 or next_i >= m or next_j >= n or grid[next_i][next_j] == 0:
                            continue 
                        if grid[next_i][next_j] not in seen_island:
                            seen_island.add(grid[next_i][next_j])
                            connect_area += island_map[grid[next_i][next_j]]

                    max_area = max(max_area, connect_area)
        return max_area



        
# @lc code=end

