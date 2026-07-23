# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res=[]
        for sub in lists:
            curr=sub
            while curr:
                res.append(curr.val)
                curr=curr.next
        res.sort()
        dummy=ListNode(0)
        curr=dummy

        for p in res:
            curr.next=ListNode(p)
            curr=curr.next
        return dummy.next



        