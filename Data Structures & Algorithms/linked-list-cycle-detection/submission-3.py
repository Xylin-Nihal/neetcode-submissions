# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        h={}
        curr=head
        while curr:
            x=curr.next
            if x in h:
                return True
            if curr not in h:
                h[curr]=1
            curr=curr.next
        return False