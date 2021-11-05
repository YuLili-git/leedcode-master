#翻转一棵二叉树。
#示例：
#输入：
#     4
#   /   \
#  2     7
# / \   / \
#1   3 6   9
#输出：
#     4
#   /   \
#  7     2
# / \   / \
#9   6 3   1
#备注:
#这个问题是受到 Max Howell 的 原问题 启发的 ：
#谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
####################### solution 1 #######################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode: 
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
####################### solution 2 #######################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode: 
        if not root:
            return root
        st = [root]
        
        while st:
            node = st.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)
        return root
####################### solution 3 #######################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode: 
        if not root:
            return root
        que = collections.deque([root])
        while que:
            for i in range(len(que)):
                node = que.popleft()
                node.left, node.right = node.right, node.left
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return root
