#给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
#你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。
#示例 1:
#输入: 
#	Tree 1                     Tree 2                  
#          1                         2                             
#         / \                       / \                            
#        3   2                     1   3                        
#       /                           \   \                      
#      5                             4   7                  
#输出: 
#合并后的树:
#	     3
#	    / \
#	   4   5
#	  / \   \ 
#	 5   4   7
######################## solution 1 ########################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 and not root2:
            return None
        if not root1:
            return root2
        if not root2:
            return root1
        root_val = root1.val + root2.val
        root = TreeNode(root_val)
        if root1.left and root2.left:
            root_left_val = root1.left.val + root1.left.val
            root.left = TreeNode(root_left_val)
            
        if root1.left:
            root.left = root1.left

        if root2.left:
            root.left = root2.left

        if root1.right and root2.right:
            root_right_val = root1.right.val + root1.right.val
            root.right = TreeNode(root_right_val)
            
        if root1.right:
            root.right = root1.right

        if root2.right:
            root.right = root2.right
            
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)
        return root
        
######################## solution 2 ########################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:

        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
######################## solution 3 ########################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        que = collections.deque()
        que.append(root1)
        que.append(root2)
        while que:
            node1 = que.popleft()
            node2 = que.popleft()
            if node1.left and node2.left:
                que.append(node1.left)
                que.append(node2.left)
            if node1.right and node2.right:
                que.append(node1.right)
                que.append(node2.right)
            node1.val += node2.val
            if not node1.left and node2.left:
                node1.left = node2.left
            if not node1.right and node2.right:
                node1.right = node2.right
        return root1
        
