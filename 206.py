# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        iterative solution
        """
        next, prev = None, None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return prev

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        recursive solution
        """
        if head == None or head.next == None:
            return head

        new_head = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return new_head
