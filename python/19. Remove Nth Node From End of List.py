# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        previous,forward,current=head,head,head
        while n:
            forward=forward.next
            n-=1
        if forward==None:
            return head.next
        while forward.next:
            forward=forward.next
            previous=previous.next
        previous.next=previous.next.next
        return current