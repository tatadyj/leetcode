#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
from collections import defaultdict


class Union_Find:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node_i, node_j):
        root_i = self.find(node_i)
        root_j = self.find(node_j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = Union_Find(len(accounts))
        email_account_map = {} # email -> id of account
        for id, account in enumerate(accounts):
            for email in account[1:]:
                if email not in email_account_map:
                    email_account_map[email] = id 
                else:
                    uf.union(id, email_account_map[email])

        email_group = defaultdict(list) # root account id -> list of emails
        for email, id in email_account_map.items():
            root_id = uf.find(id)
            email_group[root_id].append(email)

        res = []
        for id in email_group.keys():
            res.append([accounts[id][0]] + sorted(email_group[id]))
        return res


        
        
# @lc code=end

