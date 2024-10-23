# LeetCode Problem: Remove Element

## Problem Description
[Link to problem](https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150)
Difficulty: Easy

## Solution

we use two poiters to solve this problem. Pointer cptr, points to the value which we currently read 
from the list. Pointer fptr, points to location to which we instert a value. We start reading from 
the beginning of the list using cptr. If nums[cptr] is equal to val, we just skip it and move forward, 
if it is not, we copy it to nums[fptr] and move forward. We can return fptr as the length of the final 
list after removing the elements