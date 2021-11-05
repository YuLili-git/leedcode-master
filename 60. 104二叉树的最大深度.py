#给定一个二叉树，找出其最大深度。
#二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#说明: 叶子节点是指没有子节点的节点。
#示例：
#给定二叉树 [3,9,20,null,null,15,7]，
#    3
#   / \
#  9  20
#    /  \
#   15   7
#返回它的最大深度 3 。

################################### solution 1 ###################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        res = []
        if not root:
            return 0
        que = collections.deque([root])
        while que:
            tmp = []
            for i in range(len(que)):
                node = que.popleft()
                tmp.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(tmp)
        return len(res)
    
################################### solution 2 ###################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.getDepth(root)
    
    def getDepth(self, node):
        if not node:
            return 0
        leftDepth = self.getDepth(node.left)
        rightDepth = self.getDepth(node.right)
        depth = 1 + max(leftDepth, rightDepth)
        return depth
    
################################### solution 3 ###################################
class solution:
    def maxdepth(self, root: treenode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxdepth(root.left), self.maxdepth(root.right))

################################### solution 4 ###################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        que = collections.deque([root])
        depth = 0
        while que:
            n = len(que)
            depth += 1
            for i in range(n):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return depth
