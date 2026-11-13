class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        low = 0
        high = len(nums) - 1
        output = 5001

        while low < high:
            mid = (low + high) // 2
            print("low, high, mid, output", low, high, mid, output)

            if nums[mid] < output:
                output = nums[mid]
            if nums[low] < output:
                output = nums[low]
            if nums[high] < output:
                output = nums[high]

            if low <= len(nums) - 1 and nums[low] <= nums[mid]:
                low = mid + 1
            elif high >= 0 and nums[mid] <= nums[high]:
                high = mid - 1
        
        return output
