#计算给定二叉树的所有左叶子之和。
#示例：
#    3
#   / \
#  9  20
#    /  \
#   15   7
#在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
########################### solution 1 ###########################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        que = collections.deque([root])
        count = 0
        while que:
            for i in range(len(que)):
                node = que.popleft()
                
                if node.left:
                    que.append(node.left)
                    if node.left.left == None and node.left.right == None:
                        count += node.left.val
                if node.right:
                    que.append(node.right)

        return count
########################### solution 2 ###########################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_leaves_num = self.sumOfLeftLeaves(root.left)
        right_leaves_num = self.sumOfLeftLeaves(root.right)
        left_num = 0
        if root.left and root.left.left == None and root.left.right == None:
            left_num += root.left.val
        return left_num + left_leaves_num + right_leaves_num

########################### solution 3 ###########################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        st = []
        st.append(root)
        res = 0
        while st:
            node = st.pop()
            if node.left and node.left.left == None and node.left.right == None:
                res += node.left.val
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)
        return res



