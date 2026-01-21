# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans=ListNode(0, head)
        h=ans
        for i in range(n):
            head=head.next
        while head:
            head=head.next
            h=h.next
        h.next=h.next.next
        return ans.next