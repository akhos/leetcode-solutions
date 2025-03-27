# LeetCode Problem: Non-overlapping Intervals

## Problem Description
[Link to problem](https://leetcode.com/problems/non-overlapping-intervals/description/?envType=study-plan-v2&envId=leetcode-75)
Difficulty: Medium

## Solution
We use a greedy approach. Affter sorting the intervals based on their start point, 
Start tracing them from the first interval, when we have two overlapping intervals, drop
the one with rightmost end point and increase the counter by one.

## Time and Space Complexity

## Special cases to test