# LeetCode Problem: Daily Temperatures

## Problem Description
[Link to problem](https://leetcode.com/problems/daily-temperatures/description/?envType=study-plan-v2&envId=leetcode-75)
Difficulty: Medium

## Solution
starting from the end of the temperatures list, insert the first item in the stack, when encountering a new number temperature[i], pop the elements from the stack, until reaching an element which is larger than temperature[i]. Then we find the answer[i] through
the difference of i and index of this element. We push temperatur[i] to the stack and continuewith temperature[i-1]

## Time and Space Complexity

## Special cases to test