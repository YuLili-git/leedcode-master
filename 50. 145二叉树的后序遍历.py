#给定一个二叉树，返回它的 后序 遍历。
#示例:
#输入: [1,null,2,3]  
#   1
#    \
#     2
#    /
#   3 
#输出: [3,2,1]
#进阶: 递归算法很简单，你可以通过迭代算法完成吗？
############################ solution 1 ############################ 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def laterorder(root):
            if not root:
                return 
            laterorder(root.left)
            laterorder(root.right)
            res.append(root.val)
            return res
        res = []
        laterorder(root)
        return res
############################ solution 2 ############################ 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        prev = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return res
