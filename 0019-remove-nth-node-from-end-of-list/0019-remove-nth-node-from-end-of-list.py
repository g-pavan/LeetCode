# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        
        while(n):
            first = first.next
            n -= 1
        
        if(first == None):
            return head.next
        
        second = head
        
        while(first.next):
            first = first.next
            second = second.next
        
        second.next = second.next.next
        
        
        
        return head