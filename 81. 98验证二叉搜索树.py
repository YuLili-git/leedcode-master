#给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
#有效 二叉搜索树定义如下：
#节点的左子树只包含 小于 当前节点的数。
#节点的右子树只包含 大于 当前节点的数。
#所有左子树和右子树自身必须也是二叉搜索树。
#示例 1：
#输入：root = [2,1,3]
#输出：true
#示例 2：
#输入：root = [5,1,4,null,null,3,6]
#输出：false
#解释：根节点的值是 5 ，但是右子节点的值是 4 。
################################## solution 1 ##################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = []
        def rever(root):
            nonlocal res
            if not root:
                return
            rever(root.left)
            res.append(root.val)
            rever(root.right)
        def is_sorted(nums):
            for i in range(1, len(nums)):
                if nums[i] <= nums[i - 1]:
                    return False
            return True

        rever(root)
        tmp = is_sorted(res)
        return tmp
################################## solution 2 ##################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        cur_max = - float("inf")
        def isValid( root):
            nonlocal cur_max
            if not root:
                return True
            is_left = isValid(root.left)
            if cur_max < root.val:
                cur_max = root.val
            else:
                return False
            is_right = isValid(root.right)
            return is_left and is_right
        return isValid(root)
################################## solution 3 ##################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        st = []
        if not root:
            return False
        cur = root
        pre = None
        while cur or st:
            if cur:
                st.append(cur)
                cur = cur.left
            else:
                cur = st.pop()
                if pre and cur.val <= pre.val:
                    return False
                pre = cur
                cur = cur.right
        return True
