#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
def dfs(graph, visited, path, idx):
    if path[idx]: # 先序遇到path True 肯定有环
        return True 

    if visited[idx]: # visited True 之前被访问过，证明已经无环， 会再次被访问是因为这个有向图，可能不连通，不是tree
        return False 

    visited[idx] = True 
    path[idx] = True 
    for next_idx in graph[idx]:
        if dfs(graph, visited, path, next_idx):
            return True 
    path[idx] = False
    return False 




class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            end, start = edge 
            graph[start].append(end)

        visited = [False] * numCourses
        path = [False] * numCourses
        for i in range(numCourses):
            if dfs(graph, visited, path, i): # 任意一个path有环 
                return False 
        return True 
# @lc code=end

