# LeetCode Problem: Merge Sorted Arrays

## Problem Description
[Link to problem](https://leetcode.com/problems/merge-sorted-array/description//)
Difficulty: Easy

## Solution

Define three pointers, one pointing to the end of nums1
one pointing to the end of nums2 and one pointing to the index of 
to be filled item in nums1 which is end of nums1 for the moment. We start
moving back to the beginning of two lists and comparing the numbers. Always put the
largest in the place poitning by ptr3 and move that pointer towards the beginnings
when reaching to the beginning of one list, stop and copy or finish

Time Complexity: O(n + m)
Space Complexity: O(1) excluding the output