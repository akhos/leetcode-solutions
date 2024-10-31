class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countDict = {}
        maxim = 0
        selectedNum = nums[0]
        for num in nums:
            if num in countDict:
                countDict[num] += 1
            else:
                countDict[num] = 1
            if countDict[num] > maxim:
                maxim = countDict[num]
                selectedNum = num
        return selectedNum