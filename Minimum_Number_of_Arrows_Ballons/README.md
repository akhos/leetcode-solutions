# LeetCode Problem: Minimum Number of Arrows To Burst Baloons

## Problem Description
[Link to problem](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/?envType=study-plan-v2&envId=top-interview-150)
Difficulty: Medium

## Solution
we need to find the overlapping intervals. All overlapping intervals, can be covered
using one Ballon. To find the overlapping intervals, we can first sort the intervals
based on their first indexes. Then find all overlappig intervals

## Time and Space Complexity
Time Complexity: O(n) when the n is the number of points in the input string
Space Complexity: O(1)

## Special cases to test