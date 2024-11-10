#
# @lc app=leetcode id=1462 lang=python3
#
# [1462] Course Schedule IV
#

# @lc code=start
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        inDegree = [0] * numCourses
        for a,b in prerequisites:
            graph[a].append(b)
            inDegree[b] += 1

        prereq_set = [set() for _ in range(numCourses)]
        queue = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
                #prereq_set[i].add(i) #把自己加入自己的先修课程

        while queue:
            curr = queue.popleft()
            for nxt in graph[curr]:
                # 加入curr和curr所有先修课程
                prereq_set[nxt].add(curr)
                for preq in prereq_set[curr]:
                    prereq_set[nxt].add(preq)

                inDegree[nxt] -= 1
                if inDegree[nxt] == 0:
                    queue.append(nxt)

        ans = []
        for p,q in queries:
            if p in prereq_set[q]:
                ans.append(True)
            else:
                ans.append(False)
        return ans

     
# @lc code=end

