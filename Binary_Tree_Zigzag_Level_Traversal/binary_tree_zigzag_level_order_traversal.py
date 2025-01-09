# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        solution: We do the normal BFS using two Stacks. The first iteration
        of nodes, we visit the children from left to right, in the next 
        iteration, we visit the nodes right to left, in every level iteration we switch the 
        direction
        '''
        zigzagS1 = deque()
        zigzagS2 = deque()
        turn = 0
        output = []

        if not root:
            return output

        zigzagS1.append(root)
        while zigzagS1 or zigzagS2:
            temp = []
            #this level is from left to right
            if turn%2 == 0:
                while(zigzagS1):
                    elem = zigzagS1.pop()
                    temp += [elem.val]
                    if elem.left:
                        zigzagS2.append(elem.left)
                    if elem.right:
                        zigzagS2.append(elem.right)
            #this level is from right to left
            if turn%2 == 1:
                while(zigzagS2):
                    elem = zigzagS2.pop()
                    temp += [elem.val]
                    if elem.right:
                        zigzagS1.append(elem.right)
                    if elem.left:
                        zigzagS1.append(elem.left)
            output.append(temp) 
            turn += 1
        return output