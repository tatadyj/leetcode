#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
def dfs(graph, visited, path, i, postorder):
    if path[i]:
        return True 

    if visited[i]:
        return False 

    visited[i] = True 
    path[i] = True 
    for next_i in graph[i]:
        if dfs(graph, visited, path, next_i, postorder):
            return True 
    path[i] = False 
    postorder.append(i)
    return False 

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            end, start = edge 
            graph[start].append(end)
        
        visited = [False] * numCourses
        path = [False] * numCourses 
        postorder = []
        for i in range(numCourses):
            if dfs(graph, visited, path, i, postorder):
                return []
        
        postorder.reverse()
        return postorder       
# @lc code=end

