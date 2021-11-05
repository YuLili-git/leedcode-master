#给定一个二叉树，判断它是否是高度平衡的二叉树。
#本题中，一棵高度平衡二叉树定义为：
#一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
#示例 1：
#输入：root = [3,9,20,null,null,15,7]
#输出：true
#示例 2：
#输入：root = [1,2,2,3,3,null,null,4,4]
#输出：false
#示例 3：
#输入：root = []
#输出：true
########################### solution 1 ###########################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        st = []
        if not root:
            return True
        st.append(root)
        while st:
            node = st.pop()
            if abs(self.getDepth(node.left) - self.getDepth(node.right)) > 1:
                return False
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)
        return True



    def getDepth(self, cur):
        if not cur:
            return 0
        st = []
        st.append(cur)
        res = 0
        depth = 0
        while st:
            node = st.pop()
            if node:
                st.append(node)
                st.append(None)
                depth += 1
                if node.left:
                    st.append(node.left)
                if node.right:
                    st.append(node.right)
            else:
                node = st.pop()
                depth -= 1
            res = max(depth, res)
        return res
########################### solution 2 ###########################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if self.get_height(root) != -1:
            return True
        else:
            return False



    def get_height(self, root):
        if not root:
            return 0
        if (left_height := self.get_height(root.left)) == -1:
            return -1
        if (right_height := self.get_height(root.right)) == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        else:
            return 1 + max(left_height, right_height)
