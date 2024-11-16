# LeetCode Problem: Rotate List

## Problem Description
[Link to problem](https://leetcode.com/problems/rotate-list/description/?envType=study-plan-v2&envId=top-interview-150)
Difficulty: Medium

## Solution
First we should find the size of the linked list. If k > size, then change k to k % size
Set two pointers, one to the head and one k nodes ahead. Move the pointers forward when the preceeding pointer reaches to the end of the linked list, set the next of preceeding node to the previous head, set head to the node after the proceeding node and set the next of proceeding node to None.


## Time and Space Complexity
Time Complexity: O(n) 
Space Complexity: O(1)

## Special cases to test
empty list
list with one node
list with two nodes
list with more than two nodes
k larger than the size of the list
k equal to 0