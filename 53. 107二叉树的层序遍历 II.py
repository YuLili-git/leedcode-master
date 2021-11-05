#给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
#例如：
#给定二叉树 [3,9,20,null,null,15,7],
#    3
#   / \
#  9  20
#    /  \
#   15   7
#返回其自底向上的层序遍历为：
#[
#  [15,7],
#  [9,20],
#  [3]
#]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return []
        que = collections.deque()
        que.append(root)
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
        return res[::-1]
