# LeetCode Problem: Construct Binary Tree From Inorder and Postorder Traversal

## Problem Description
[Link to problem](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/?envType=study-plan-v2&envId=top-interview-150)
Difficulty: Medium

## Solution
The postorder traversal, always ends with the root or the tree. Because we first traverse
the left subtree, then the right subtree and at the end the root. Therfore, the last element
of postorder list is the root of the tree. We find the last order of postorder in the inorder. Sine it is the root, in inoder, it divides the input to the left and right subtree 
lists. Because in inorder traversal, we first traverse the left subtree, then the root and 
then the right subtree. After finding the root and the nodes in the left and right subtrees,
we can recursively beuild the roots of the left and right subtrees and continue, until the
lists are empty or have one elemennt

## Time and Space Complexity

## Special cases to test