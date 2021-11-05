#给定一棵二叉树的根节点 root ，请找出该二叉树中每一层的最大值。
#示例1：
#输入: root = [1,3,2,5,3,null,9]
#输出: [1,3,9]
#解释:
#          1
#         / \
#        3   2
#       / \   \  
#      5   3   9 
#示例2：
#输入: root = [1,2,3]
#输出: [1,3]
#解释:
#          1
#         / \
#        2   3
#示例3：
#输入: root = [1]
#输出: [1]
#示例4：
#输入: root = [1,null,2]
#输出: [1,2]
#解释:      
#           1 
#            \
#             2     
#示例5：
#输入: root = []
#输出: []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return []
        que = collections.deque([root])
        while que:
            tmp = []
            for i in range(len(que)):
                node = que.popleft()
                tmp.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(max(tmp))
        return res
