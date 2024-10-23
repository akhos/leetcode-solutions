# LeetCode Problem: Remove Duplicated from Sorted Array

## Problem Description
[Link to problem](https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150)
Difficulty: Easy

## Solution
To solve this problem we can use a dictionary, a pointer for reading list elements and 
a counter numPtr counting the number of elements in the final list. 
While reading the initial list elements, we check if the element exists in the dictionary, if not
we add it to the dictionary with a value such as 1. We insert it in to num[numPtr] and increas numPtr.
We continue this to reach the end of the list. Since the list is sorted, we could also solve this 
problem without using dictionary. It would improve the memory usage O(1).

Time Complexity: O(n)
Space complexity O(n)