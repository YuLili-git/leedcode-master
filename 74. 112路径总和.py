#给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。
#叶子节点 是指没有子节点的节点。
#示例 1：
#输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
#输出：true
#示例 2：
#输入：root = [1,2,3], targetSum = 5
#输出：false
#示例 3：
#输入：root = [1,2], targetSum = 0
#输出：false
############################# solution 1 #############################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def isornot( cur, target):
            if not cur.left and not cur.right and target == 0:
                return True 
            if not cur.left and not cur.right:
                return False
            if cur.left:
                target -=  cur.left.val
                if isornot(cur.left, target):
                    return True
                target += cur.left.val

            if cur.right:
                target -= cur.right.val
                if isornot(cur.right, target):
                    return True
                target += cur.right.val
            return False
        if root == None:
            return False
        else:
            return isornot(root, targetSum - root.val)

############################# solution 2 #############################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = []
        stack.append((root, root.val))
        while stack:
            cur_node, path_sum = stack.pop()
            if not cur_node.left and not cur_node.right and path_sum == targetSum:
                return True
            if cur_node.left:
                stack.append((cur_node.left, path_sum + cur_node.left.val))
            if cur_node.right:
                stack.append((cur_node.right, path_sum + cur_node.right.val))
        return False
