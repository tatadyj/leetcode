#
# @lc app=leetcode id=558 lang=python3
#
# [558] Logical OR of Two Binary Grids Represented as Quad-Trees
#

# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf and quadTree2.isLeaf:
            node = Node(quadTree1.val | quadTree2.val, True, None, None, None, None)
            return node 
        
        if (quadTree1.isLeaf and quadTree1.val) or (quadTree2.isLeaf and quadTree2.val):
            node = Node(True, True, None, None, None, None)
            return node 


        # isLeaf == True, val == 0, 
        # or isLeaft == False
        A = quadTree1 if quadTree1.isLeaf else quadTree1.topLeft
        B = quadTree2 if quadTree2.isLeaf else quadTree2.topLeft
        topLeft = self.intersect(A, B)

        A = quadTree1 if quadTree1.isLeaf else quadTree1.topRight
        B = quadTree2 if quadTree2.isLeaf else quadTree2.topRight
        topRight = self.intersect(A, B)

        A = quadTree1 if quadTree1.isLeaf else quadTree1.bottomLeft
        B = quadTree2 if quadTree2.isLeaf else quadTree2.bottomLeft
        bottomLeft = self.intersect(A, B)

        A = quadTree1 if quadTree1.isLeaf else quadTree1.bottomRight
        B = quadTree2 if quadTree2.isLeaf else quadTree2.bottomRight
        bottomRight = self.intersect(A, B)

        if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf \
            and (topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
            node = Node(topLeft.val, True, None, None, None, None)
            return node
        else:
            node = Node(topLeft.val, False, None, None, None, None)
            node.topLeft = topLeft
            node.topRight = topRight
            node.bottomLeft = bottomLeft
            node.bottomRight = bottomRight 
            return node 
# @lc code=end

