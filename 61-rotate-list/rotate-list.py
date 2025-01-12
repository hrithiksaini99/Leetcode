# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        # First, find the length of the list
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        # Make the list circular
        current.next = head
        
        # Effective rotations needed
        k = k % length
        if k == 0:
            current.next = None  # Break the circular link
            return head
        
        # Find the new tail: (length - k - 1)th node
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        # The new head is the next node after the new tail
        new_head = new_tail.next
        
        # Break the circular link
        new_tail.next = None
        
        return new_head