class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cptr = fptr = 0
        while cptr < len(nums):
            if nums[cptr] != val:
                nums[fptr] = nums[cptr]
                fptr += 1
            cptr += 1
        
        return fptr