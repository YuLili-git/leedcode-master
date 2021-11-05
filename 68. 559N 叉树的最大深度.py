#给定一个 N 叉树，找到其最大深度。
#最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
#N 叉树输入按层序遍历序列化表示，每组子节点由空值分隔（请参见示例）。
#示例 1：
#输入：root = [1,null,3,2,4,null,5,6]
#输出：3
#示例 2：
#输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
#输出：5
#提示：
#树的深度不会超过 1000 。
#树的节点数目位于 [0, 104] 之间。
####################### solution 1 #######################
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        res = []
        if not root:
            return 0
        from collections import deque
        que = deque([root])
        while que:
            tmp = []
            for i in range(len(que)):
                node = que.popleft()
                tmp.append(node.val)
                if node.children:
                    que.extend(node.children)
            res.append(tmp)
        return len(res)

####################### solution 2 #######################
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        depth = 0
        for i in range(len(root.children)):
            depth = max(depth, self.maxDepth(root.children[i]))
        return depth + 1

####################### solution 3 #######################
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        que = collections.deque([root])
        depth = 0
        while que:
            depth += 1
            for i in range(len(que)):
                node = que.popleft()
                for j in range(len(node.children)):
                    if node.children[j]:
                        que.append(node.children[j])
        return depth


####################### solution 4 #######################
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        st = []
        res = 0
        depth = 0
        if root:
            st.append(root)
        while st:
            node = st.pop()
            if node != None:
                st.append(node)
                st.append(None)
                depth += 1
                for i in range(len(node.children)):
                    if node.children[i]:
                        st.append(node.children[i])
            else:
                node = st.pop()
                depth -= 1
            res = max(res, depth)
        return res
        
