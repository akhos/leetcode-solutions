# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        '''
        The postorder traversal, always ends with the root or the tree. Because we first traverse
        the left subtree, then the right subtree and at the end the root. Therfore, the last element
        of postorder list is the root of the tree. We find the last order of postorder in the 
        inorder. Sine it is the root, in inoder, it divides the input to the left and right subtree 
        lists. Because in inorder traversal, we first traverse the left subtree, then the root and 
        then the right subtree. After finding the root and the nodes in the left and right subtrees,
        we can recursively beuild the roots of the left and right subtrees and continue, until the
        lists are empty or have one elemennt
        '''
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        if len(inorder) == 0:
            return None
        #find the last element of postorder, set it as the root
        #divide the inorder list based on the last element to find the nodes in the 
        # left and right subtrees. Divide the postorder based on the nodes in left and right
        # subtrees and continue recusively
        root = TreeNode(postorder[-1])
        index = 0
        while inorder[index] != root.val:
            index += 1
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1]) 
        return root
        