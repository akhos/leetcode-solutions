# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        '''
        we can trace DFS the trees, and when reaching to leafs we register them in the list. 
        This gives the left to right order of the leafs. Then we compare both left to write orders of the 
        leafs for the trees to check if they are equal or not
        '''
        lst1 = []
        lst2 = []
        self.leftToRight(root1, lst1)
        self.leftToRight(root2, lst2)
        return lst1 == lst2 
    def leftToRight(self, root: Optional[TreeNode], lst: List[int]):
        if root.left:
            self.leftToRight(root.left, lst)
        if root.right:
            self.leftToRight(root.right, lst)
        if not root.left and not root.right:
            lst.append(root.val)
        return