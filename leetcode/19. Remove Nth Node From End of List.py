# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # using two pointer slow and fast
        # when fast is at end, so slow is the node need to be removed
        # so first let fast move n+1 steps away
        # that way, at the end, slow.next is the node need to be removed
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        for _ in range(n+1):
            fast = fast.next 
        
        while fast:
            slow = slow.next 
            fast = fast.next 
        
        slow.next = slow.next.next 
        return dummy.next