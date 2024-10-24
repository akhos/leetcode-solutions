# LeetCode Problem: Longest Common Prefix

## Problem Description
[Link to problem](https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150)
Difficulty: Easy

## Solution
We should compare all the characters of index i in all the strings to each other. Starting from index 0 and increasing one by one, we check the letters all the strings, when we reach to the end of one of one of the strings, or when we encounter a mismatch, it means that we found the longest common prefix

## Time and Space Complexity
Time Complexity: O(n*m) where n is the number of words in the list and m is the length of the longest prefix
Space Complexity: O(1) 

## Special cases to test
In addition to normal case of a word having a number of words with longest common string of length 1 or more, we need to test the case when the longest common string has length 0, we need to check the case when the list of words has only one sentence. We also need to test a case when one of the sentences is empty sentence. We should check the case when one of the words is one space.