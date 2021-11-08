#给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
#假定 BST 有如下定义：
#结点左子树中所含结点的值小于等于当前结点的值
#结点右子树中所含结点的值大于等于当前结点的值
#左子树和右子树都是二叉搜索树
#例如：
#给定 BST [1,null,2,2],
#   1
#    \
#     2
#    /
#   2
#返回[2].
######################### solution 1 #########################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        que = collections.deque([root])
        dic = {}
        while que:
            for i in range(len(que)):
                node = que.popleft()
                if node.val not in dic:
                    dic[node.val] = 1
                else:
                    dic[node.val] += 1
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        tmp = []
        max_num = 0
        for i, j in dic.items():
            if j > max_num:
                max_num = j
        for i in dic.keys():
            if dic[i] == max_num:
                tmp.append(i)
        return tmp
######################### solution 2 #########################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = TreeNode()
        self.count = 0
        self.max_count = 0
        self.result = []
             
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        self.search_BST(root)
        return self.result
    
    def search_BST(self, root: TreeNode):
        if not root:
            return None
        self.search_BST(root.left)
        if not self.pre:
            self.count = 1
        elif self.pre.val == root.val:
            self.count += 1
        else:
            self.count = 1
        self.pre = root
        if self.count == self.max_count:
            self.result.append(root.val)

        if self.count > self.max_count:
            self.max_count = self.count
            self.result = [root.val]

        self.search_BST(root.right)

######################### solution 3 #########################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        st = []
        cur = root
        pre = None
        count = 0
        max_count = 0
        res = []
        while cur or st:
            if cur:
                st.append(cur)
                cur = cur.left
            else:
                cur = st.pop()
                if pre == None:
                    count = 1
                elif pre.val == cur.val:
                    count += 1
                else:
                    count = 1
                
                if count == max_count:
                    res.append(cur.val)
                if count > max_count:
                    max_count = count
                    res.clear()
                    res.append(cur.val)
                pre = cur
                cur = cur.right
        return res
