#
# @lc app=leetcode id=2876 lang=python3
#
# [2876] Count Visited Nodes in a Directed Graph
#

# @lc code=start
class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        """
        对于任何有向图而言，顺着边的方向走向去，只有两种归宿：要么进入死胡同，要么进入循环圈。
        所以你可以把有向图简单地认为就是若干个单链并入一个环。
        我们先找出入度为零的节点，然后用拓扑排序的方法将所有单链上的节点排除掉。
        剩下的就是环上的节点。从环的任意节点出发，可以遍历整个环得到环的长度（也就是对于这些节点的答案）。
        最后再遍历单链节点，dfs直至遇到环的入口，这段距离加上环的长度，就是对于这些节点的答案。
        
        """
        n = len(edges)
        in_degree = [0] * n

        for i in range(n):
            in_degree[edges[i]] += 1

        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()
            nxt = edges[curr]
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

        res = [0] * n
        for i in range(n):
            if in_degree[i] == 0: continue 
            if res[i] != 0: continue 
            j = i
            L = 1
            while edges[j] != i:
                j = edges[j]
                L += 1
            j = i 
            while edges[j] != i:
                res[j] = L 
                j = edges[j]


        def dfs(curr):
            if res[curr] != 0:
                return res[curr]

            res[curr] = dfs(edges[curr]) + 1
            return res[curr]

        for i in range(n):
            if in_degree[i] != 0: continue 
            dfs(i)         
        return res   
        
# @lc code=end

