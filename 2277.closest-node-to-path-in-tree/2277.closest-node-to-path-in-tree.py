#
# @lc app=leetcode id=2277 lang=python3
#
# [2277] Closest Node to Path in Tree
#

# @lc code=start
class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        adj_dict = defaultdict(list)
        for a, b in edges:
            adj_dict[a].append(b)
            adj_dict[b].append(a)

        def dfs(curr, prev, target):
            if curr == target:
                ans.append(path[:])
                return True 
            
            for nxt in adj_dict[curr]:
                if nxt == prev: continue 
                path.append(nxt)
                if dfs(nxt, curr, target):
                    return True 
                path.pop()
            return False

        ans = []
        for start, end, _ in query:
            path = [start]
            dfs(start, -1, end)
        #print(ans)
        

        def dfs_dist(curr, prev, dist):
            nonlocal min_dist, min_node
            for nxt in adj_dict[curr]:
                if nxt == prev: continue
                if nxt in all_nodes:
                    if min_dist > dist + 1:
                        min_dist = dist + 1
                        min_node = nxt
                dfs_dist(nxt, curr, dist+1)
        
        ret = []
        for i, (_, _, node) in enumerate(query):
            all_nodes = set(ans[i])
            if node in all_nodes:
                min_dist = 0
                ret.append(node)
            else:
                min_dist = float('inf')
                min_node = None
                dfs_dist(node, -1, 0)
                ret.append(min_node)
        
        return ret
   
# @lc code=end

