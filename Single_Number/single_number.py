class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        XOR all the elements, the duplicate ones make the result 0 and the result will be 
        the remaining number
        '''
        number = nums[0]
        for i in range(1, len(nums)):
            number = number ^ nums[i]
        return number