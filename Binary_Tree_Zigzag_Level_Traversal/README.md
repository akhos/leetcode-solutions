# LeetCode Problem: Binary Tree Zigzag Level Order Traversal

## Problem Description
[Link to problem](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/?envType=study-plan-v2&envId=top-interview-150)
Difficulty: Medium

## Solution
We do the normal BFS using two Stacks. The first iteration
of nodes, we visit the children from left to right, in the next 
iteration, we visit the nodes right to left, in every level iteration we switch the 
direction

## Time and Space Complexity
Time Complexity: O(n) when the n is the number of nodes in the input
Space Complexity: O(n)

## Special cases to test