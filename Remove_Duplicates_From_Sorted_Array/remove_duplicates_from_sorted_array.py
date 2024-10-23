class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numDict = {}
        numPtr = 0
        for num in nums:
            if num not in numDict:
                numDict[num] = 1
                nums[numPtr] = num
                numPtr += 1
        return numPtr