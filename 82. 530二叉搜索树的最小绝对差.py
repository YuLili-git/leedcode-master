#给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
#差值是一个正数，其数值等于两值之差的绝对值。
#示例 1：
#输入：root = [4,2,6,1,3]
#输出：1
#示例 2：
#输入：root = [1,0,48,null,null,12,49]
#输出：1
################################ solution 1 ################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = []
        def inorder(root):
            if not root:
                return 
            
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            return res
        inorder(root)

        count = float("inf")
        for i in range(1, len(res)):
            count = min(count, abs(res[i] - res[i - 1]))
        return count
        

################################ solution 2 ################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        st = []
        cur = root
        pre = None
        res = float("inf")
        while st or cur:
            if cur:
                st.append(cur)
                cur = cur.left
            else:
                cur = st.pop()
                if pre:
                    res = min(res, cur.val - pre.val)
                pre = cur
                cur = cur.right
        return res


