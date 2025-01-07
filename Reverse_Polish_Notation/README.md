# LeetCode Problem: Evaluat Reverse Polish Notatio

## Problem Description
[Link to problem](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/?envType=study-plan-v2&envId=top-interview-150)
Difficulty: Medium

## Solution
start checking the tokens from the beginning of the tokens list,
when we encounter an operand, push it into the stack, when we encounter an 
operation, we pop two numbers from the stack, apply the operation on them and push
the result into the stack, when we reach to the end of the tokens list, the final result
is on top of the stack

## Time and Space Complexity
Time Complexity: O(n) when the n is length of the input string
Space Complexity: O(n)

## Special cases to test