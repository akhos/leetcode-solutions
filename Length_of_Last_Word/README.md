# LeetCode Problem: Length Of Last Word

## Problem Description
[Link to problem]()https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150
Difficulty: Easy

## Solution

First remove the with spaces at the end of the string. Check the characters from the beginning of the string.
When encounter a non space character, increase the counter, when reaching to space, reset the counter to 0. Return the 
last counter value

## Time and Space Complexity
Time Complexity: O(n) where n is the number of character
Space Complexity: O(1) 

## Special cases to test
In addition to normal sentences, we need to test sentence with more than one consecutive space, sentence beginning and 
ending with spaces empty sentence and Sentence which is only consist of space.