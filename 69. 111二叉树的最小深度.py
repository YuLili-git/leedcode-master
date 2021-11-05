#给定一个二叉树，找出其最小深度。
#最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#说明：叶子节点是指没有子节点的节点。
#示例 1：
#输入：root = [3,9,20,null,null,15,7]
#输出：2
#示例 2：
#输入：root = [2,null,3,null,4,null,5,null,6]
#输出：5
############################ solution 1 ############################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        res = []
        if not root:
            return 0
        que = [(root, 1)]
        while que:
            cur, depth = que.pop(0)
            if cur.left == None and cur.right == None:
                return depth
            if cur.left:
                que.append((cur.left, depth + 1))
            if cur.right:
                que.append((cur.right, depth + 1))
        return 0

############################ solution 2 ############################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        min_depth = 10 ** 9
        if root.left:
            min_depth = min (self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)
        return min_depth + 1

############################ solution 3 ############################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        que = collections.deque([root])
        res = 1
        while que:
            for i in range(len(que)):
                node = que.popleft()
                if not node.left and not node.right:
                    return res
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
            res += 1
        return res
