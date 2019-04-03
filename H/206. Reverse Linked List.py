# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []
        def reverse(node):
            if node is None:
                return

            stack.insert(0, node.val)
            reverse(node.next)
            node.val = stack.pop()

        reverse(head)
        return head