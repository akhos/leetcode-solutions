# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        counter = 1
        ptr = head
        while ptr.next:
            ptr = ptr.next
            counter+=1
        
        k%=counter

        if k == 0:
            return head
        ptr = ListNode(0)
        ptr.next = head
        ptrFor = head
        counter = 1
        while counter < k:
            counter+=1
            ptrFor = ptrFor.next
        
        while ptrFor.next:
            ptrFor = ptrFor.next
            ptr = ptr.next
        ptrFor.next = head
        head = ptr.next
        ptr.next = None
        return head