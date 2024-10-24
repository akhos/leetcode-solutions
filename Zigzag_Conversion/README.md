# LeetCode Problem: Zigzag Conversion

## Problem Description
[Link to problem](https://leetcode.com/problems/zigzag-conversion/description/?envType=study-plan-v2&envId=top-interview-150)
Difficulty: Medium

## Solution
We create a list of lists. This list, contains numRows strings, each of them is
initially empty. As we continue reading the input string s, character by character, 
we add the characters to these strings. We start from the first strings, adding one character to 
each string till we reach to the last string. Then we reverse back, adding one character to each string, till
we reach to the first string. This process is continued till we process all the characters in the string.  At the end we attach the lists in words together and return the final string


## Time and Space Complexity
Time Complexity: O(n) when the n is the number of characters in the first string
Space Complexity: O(n)

## Special cases to test
In addition to the normal case when we have a string with numRows grater than 1, we shoud check
- empty string numRows greater than 1
- a string and numRows 1
- Special cases when numRows is negative