#给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。
#完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
#示例 1：
#输入：root = [1,2,3,4,5,6]
#输出：6
#示例 2：
#输入：root = []
#输出：0
#示例 3：
#输入：root = [1]
#输出：1
#提示：
#树中节点的数目范围是[0, 5 * 104]
#0 <= Node.val <= 5 * 104
#题目数据保证输入的树是 完全二叉树
################################# solution 1 #################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        que = collections.deque([root])
        count = 1
        while que:
            for i in range(len(que)):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                    count += 1
                if node.right:
                    que.append(node.right)
                    count += 1
        return count

################################# solution 2 #################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_num = self.countNodes(root.left)
        right_num = self.countNodes(root.right)
        sum_num = left_num + right_num
        return sum_num + 1

################################# solution 3 #################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = root.left
        right = root.right
        leftHeight = 0
        rightHeight = 0
        while left:
            left = left.left
            leftHeight += 1
        while right:
            right = right.right
            rightHeight += 1
        if leftHeight == rightHeight:
            return (2 << leftHeight) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
