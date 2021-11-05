#给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。
#示例 1：
#输入：
#    3
#   / \
#  9  20
#    /  \
#   15   7
#输出：[3, 14.5, 11]
#解释：
#第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        if not root:
            return []
        que = collections.deque()
        que.append(root)
        while que:
            count = 0
            n = len(que)
            for i in range(n):
                node = que.popleft()
                count += node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(count / n)
        return res
