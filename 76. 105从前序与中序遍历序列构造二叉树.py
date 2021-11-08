#给定一棵树的前序遍历 preorder 与中序遍历  inorder。请构造二叉树并返回其根节点。
#示例 1:
#Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
#Output: [3,9,20,null,null,15,7]
#示例 2:
#Input: preorder = [-1], inorder = [-1]
#Output: [-1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)

        root_index = inorder.index(root_val)
        inorder_left = inorder[ : root_index]
        inorder_right = inorder[root_index + 1 : ]

        preorder_left = preorder[1 : 1 + len(inorder_left)]
        preorder_right = preorder[1 + len(inorder_left) :]

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)
        return root
        
