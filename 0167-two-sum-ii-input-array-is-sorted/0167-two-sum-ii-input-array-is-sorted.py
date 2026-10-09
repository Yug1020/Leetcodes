class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers) - 1
        left = 0
        right = n

        while numbers[right] + numbers[left] != target:            
            if numbers[right] + numbers[left] < target:
                left += 1
            
            if numbers[right] + numbers[left] > target:
                right -= 1
            
        return [left + 1, right + 1]