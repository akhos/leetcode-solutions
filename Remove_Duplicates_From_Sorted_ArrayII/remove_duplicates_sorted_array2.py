class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return -1
        
        currentPtr = 1
        lstPtr = 0
        counter = 1
        while currentPtr < len(nums):
            if nums[lstPtr] != nums[currentPtr]:
                lstPtr+= 1
                nums[lstPtr] = nums[currentPtr]
                counter = 1
            elif counter < 2:
                lstPtr+= 1
                nums[lstPtr] = nums[currentPtr]
                counter+= 1
            
            currentPtr+= 1
        return lstPtr + 1