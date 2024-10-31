class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        r = len(nums) - k
        nums[:] = nums[r:] + nums[:r]