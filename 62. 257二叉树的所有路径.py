#给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
#叶子节点 是指没有子节点的节点。
#示例 1：
#输入：root = [1,2,3,null,5]
#输出：["1->2->5","1->3"]
#示例 2：
#输入：root = [1]
#输出：["1"]
########################### solution 1 ###########################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        path = ''
        res = []
        self.traversal(root, path, res)
        return res

    def traversal(self, cur: TreeNode, path: str, res: List[str]):
        path += str(cur.val)
        if not cur.left and not cur.right:
            res.append(path)
        if cur.left:
            self.traversal(cur.left, path + '->', res)
        if cur.right:
            self.traversal(cur.right, path + '->', res)


########################### solution 2 ###########################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        from collections import deque
        st = deque([root])
        path_st = deque()
        res = []
        path_st.append(str(root.val))
        while st:
            node = st.pop()
            path = path_st.pop()
            if not (node.left or node.right):
                res.append(path)
            if node.right:
                st.append(node.right)
                path_st.append(path + '->' + str(node.right.val))
            if node.left:
                st.append(node.left)
                path_st.append(path + '->' + str(node.left.val))
            
        return res
