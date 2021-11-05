#给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
#示例：
#二叉树：[3,9,20,null,null,15,7],
#    3
#   / \
#  9  20
#    /  \
#   15   7
#返回其层序遍历结果：
#[
#  [3],
#  [9,20],
#  [15,7]
#]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return []
        from collections import deque
        que = deque([root])
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
        return res
