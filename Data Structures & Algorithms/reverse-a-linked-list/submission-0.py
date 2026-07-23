# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        lst=[]
        while temp:
            lst.append(temp.val)
            temp=temp.next
        lst.reverse()
        dummy = ListNode(0)
        curr = dummy

        for x in lst:
            curr.next = ListNode(x)
            curr = curr.next

        return dummy.next
        


        