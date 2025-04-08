# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        A = head
        tmp = A
        B = A.next
        tmp2 = B.next
        B.next = tmp
        tmpHead = B
        A.next = self.swapPairs(tmp2)
        return tmpHead