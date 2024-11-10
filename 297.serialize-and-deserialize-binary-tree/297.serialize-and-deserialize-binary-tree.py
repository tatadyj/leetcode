#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

def preorder(curr, ans):
    if not curr:
        ans.append('#')
        return 
    ans.append(str(curr.val))
    preorder(curr.left, ans)
    preorder(curr.right, ans)

def recur(queue):
    if not queue:
        return 

    val = queue.popleft()
    if val == '#':
        return
            
    curr = TreeNode(val)
    curr.left = recur(queue)
    curr.right = recur(queue)

    return curr

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #ans = []
        #preorder(root, ans)
        #return ''.join(ans)
        
        # bfs
        '''
        if not root: 
            return ''

        ans = []
        queue = deque([root])
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                if curr:
                    ans.append(str(curr.val))
                    queue.append(curr.left)
                    queue.append(curr.right)
                else:
                    ans.append('')

        while ans and ans[-1] == '':
            ans.pop()

        return ','.join(ans)
        '''
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #queue = deque(data)
        #return recur(queue)

        # bfs 
        if data == '': return None

        queueRight = deque([TreeNode(int(v)) if v != '' else None for v in data.split(',')])
        root = queueRight.popleft()
        queueLeft = deque([root])
        while queueLeft:
            size = len(queueLeft)
            for _ in range(size):
                curr = queueLeft.popleft()
                if queueRight:
                    curr.left = queueRight.popleft()
                else:
                    curr.left = None
                if queueRight:
                    curr.right = queueRight.popleft()
                else:
                    curr.right = None

                if curr.left:
                    queueLeft.append(curr.left)
                if curr.right:
                    queueLeft.append(curr.right)
             
        return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# @lc code=end

