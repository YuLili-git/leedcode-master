#根据一棵树的中序遍历与后序遍历构造二叉树。
#注意:
#你可以假设树中没有重复的元素。
#例如，给出
#中序遍历 inorder = [9,3,15,20,7]
#后序遍历 postorder = [9,15,7,20,3]
#返回如下的二叉树：
#    3
#   / \
#  9  20
#    /  \
#   15   7
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        root_val = postorder[-1]
        root = TreeNode(root_val)

        root_index = inorder.index(root_val)
 
        inorder_left = inorder[: root_index]
        inorder_right = inorder[root_index + 1 : ]

        postorder_left = postorder[ : len(inorder_left)]
        postorder_right = postorder[len(inorder_left):-1]

        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)
        return root
        
