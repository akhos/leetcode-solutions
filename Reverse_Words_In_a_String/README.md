# LeetCode Problem: Reverse Words in a String

## Problem Description
[Link to problem](https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150)
Difficulty: Medium

## Solution
First we remove the space characters from the beginning and end of the string. Then we start tracing from the beginning of the string and find the words in the string, store them in a list. The list contains the set of words in the string. We start from the end of the list, we extract the words and attach them together with one space between every two consecutive words. For extracting words from the string, whenever encountring a space, we extract the word from previous space to that space and store it in the list. 

## Time and Space Complexity
Time Complexity: O(n) where n is the number of characters in a string
Space Complexity: O(n) 

## Special cases to test
In addition to the normal case of a string, we need to check the following cases:
- when there are more than one spaces splitting the words in the string
- Empty string
- String with only one word
- String with spaces at start and end