# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        do DFS using a stack. We keep another stack which holds the max number in the stack.
        While traversing, when we pop a node, we check if the max is greater than it or not.
        if not, then the node is a good node. If yes, it is not.
        '''
        if not root:
            return 0
        counter = 0
        nodeStack = deque()
        maxStack = deque()
        nodeStack.append(root)
        maxStack.append(root.val)
        while nodeStack:
            node = nodeStack.pop()
            maxi = maxStack.pop()
            if node.val >= maxi:
                counter += 1
            if node.right:
                nodeStack.append(node.right)
                maxStack.append(max(maxi, node.right.val))
            if node.left:
                nodeStack.append(node.left)
                maxStack.append(max(maxi, node.left.val))
        return counter