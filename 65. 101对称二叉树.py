#给定一个二叉树，检查它是否是镜像对称的。
#例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#    1
#   / \
#  2   2
# / \ / \
#3  4 4  3
#但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#    1
#   / \
#  2   2
#   \   \
#   3    3
#进阶：
#你可以运用递归和迭代两种方法解决这个问题吗？
###################### solution 1 ######################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compare(self, left, right):
        if left == None and right == None:
            return True
        elif left != None and right == None:
            return False
        elif left == None and right != None:
            return False
        elif left.val != right.val:
            return False
        return self.compare(left.left, right.right) and self.compare(left.right, right.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)

###################### solution 2 ######################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        que = collections.deque()
        que.append(root.left)
        que.append(root.right)
        while que:
            leftNode = que.popleft()
            rightNode = que.popleft()
            if not leftNode and not rightNode :
                continue
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            que.append(leftNode.left)
            que.append(rightNode.right)
            que.append(leftNode.right)
            que.append(rightNode.left)
        return True

###################### solution 3 ######################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        que = []
        que.append(root.left)
        que.append(root.right)
        while que:
            leftNode = que.pop()
            rightNode = que.pop()
            if not leftNode and not rightNode :
                continue
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            que.append(leftNode.left)
            que.append(rightNode.right)
            que.append(leftNode.right)
            que.append(rightNode.left)
        return True
