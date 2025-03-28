
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        '''
        One solution would be to count the number of nodes; n. Then we create a list of size n/2. We start 
        by adding the elements and their twins to the list while we traverse and keep the maximum. 
        The running time is O(n) and the space is O(n). We can do this also in one pass, using two pointers
        '''
        tmp = head
        counter = 1
        while tmp.next:
            tmp = tmp.next
            counter += 1
        
        tmp = head
        lst = []
        for i in range(counter // 2):
            lst.append(tmp.val)
            tmp = tmp.next
        
        maxi = tmp.val + lst[-1]
        for i in range(counter//2 - 1, -1 , -1):
            maxi = max(maxi, lst[i] + tmp.val)
            tmp = tmp.next
        
        return(maxi)