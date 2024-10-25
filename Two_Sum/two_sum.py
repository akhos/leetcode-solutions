class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftIndex = 0
        rightIndex = len(numbers) - 1
        summed = numbers[leftIndex] + numbers[rightIndex]
        while ( summed != target):
            if summed > target:
                rightIndex -= 1
            else:
                leftIndex += 1
            summed = numbers[leftIndex] + numbers[rightIndex]
        return[leftIndex + 1, rightIndex + 1]
