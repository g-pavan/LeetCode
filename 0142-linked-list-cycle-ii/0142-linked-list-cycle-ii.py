# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow = fast = head
        while True:
            slow = slow.next
            fast = fast.next
            if fast == None or fast.next == None:
                return None
            else:
                fast = fast.next
            if slow==fast:
                meet = fast
                break
        p1=head
        p2=meet
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1   