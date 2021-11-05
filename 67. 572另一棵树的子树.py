#给你两棵二叉树 root 和 subRoot 。检验 root 中是否包含和 subRoot 具有相同结构和节点值的子树。如果存在，返回 true ；否则，返回 false 。
#二叉树 tree 的一棵子树包括 tree 的某个节点和这个节点的所有后代节点。tree 也可以看做它自身的一棵子树。
#示例 1：
#输入：root = [3,4,5,1,2], subRoot = [4,1,2]
#输出：true
#示例 2：
#输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
#输出：false
#提示：
#root 树上的节点数量范围是 [1, 2000]
#subRoot 树上的节点数量范围是 [1, 1000]
#-104 <= root.val <= 104
#-104 <= subRoot.val <= 104
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def identical(self, nodea, nodeb):
        if not nodea and not nodeb:
            return True
        if nodea is None or nodeb is None:
            return False
        return nodea.val == nodeb.val and self.identical(nodea.left, nodeb.left) and self.identical(nodea.right, nodeb.right)

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root:
            return False
        if self.identical(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
