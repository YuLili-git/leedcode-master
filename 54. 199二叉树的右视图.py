#给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#示例 1:
#输入: [1,2,3,null,5,null,4]
#输出: [1,3,4]
#示例 2:
#输入: [1,null,3]
#输出: [1,3]
#示例 3:
#输入: []
#输出: []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return []
        que = collections.deque()
        que.append(root)
        while que:
            tmp = []
            for i in range(len(que)):
                node = que.popleft()
                tmp.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(tmp[-1])
        return res
