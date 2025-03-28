# LeetCode Problem: Count Good Nodes in Binary Tree

## Problem Description
[Link to problem](https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75)
Difficulty: Medium

## Solution
do DFS using a stack. We keep another stack which holds the max number in the stack.
While traversing, when we pop a node, we check if the max is greater than it or not.
if not, then the node is a good node. If yes, it is not.

## Time and Space Complexity

## Special cases to test