# LeetCode Problem: Is subsequence

## Problem Description
[Link to problem](https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150)
Difficulty: Easy

## Solution
if the string s is empty string, it is a subsequence of t. Otherwise, starting from index 0, when we find s[index] in t, if 
s[index] == t[j], we will look for s[index + 1] in t[j + 1:]. We continue until we find a match for all the characters in s or 
we reach to the end of string t. 

## Time and Space Complexity
Time Complexity: O(n + m) when n is the number of characters in the string t and m is the number of characters in string s.
Space Complexity: O(1)

## Special cases to test

