#给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。
#假设二叉树中至少有一个节点。
#示例 1:
#输入: root = [2,1,3]
#输出: 1
#示例 2:
#输入: [1,2,3,4,null,5,6,null,null,7]
#输出: 7

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return 0
        que = collections.deque([root])
        res = root.val
        while que:
            for i in range(len(que)):
                node = que.popleft()
                if i == 0:
                    res = node.val              
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return res
