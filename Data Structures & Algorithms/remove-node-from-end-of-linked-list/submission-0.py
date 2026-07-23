# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lst=[]
        while head:
            lst.append(head.val)
            head=head.next
        lst.pop(-n)
        dummy=ListNode(0)
        curr=dummy

        for p in lst:
            curr.next=ListNode(p)
            curr=curr.next
        return dummy.next
        
        
        