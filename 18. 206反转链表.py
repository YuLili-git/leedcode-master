#给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
#示例 1：
#输入：head = [1,2,3,4,5]
#输出：[5,4,3,2,1]
#示例 2：
#输入：head = [1,2]
#输出：[2,1]
#示例 3：
#输入：head = []
#输出：[]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def revers(pre, cur):
            if not cur:
                return pre
            res = cur.next
            cur.next = pre
            return revers(cur, res)
        return revers(None, head)
