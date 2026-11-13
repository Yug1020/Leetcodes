class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        lowerOutput = 10**4

        def lowerBound(low, high, target, lowerOutput):
            if low > high:
                if low < lowerOutput:
                    lowerOutput = low
                return lowerOutput         
            elif high < low:
                return 0

            if nums[low] == target:
                if low < lowerOutput:
                    lowerOutput = low
                return lowerOutput

            mid = (low + high) // 2

            if nums[mid] < target:
                return lowerBound(mid+1, high, target, lowerOutput)
            
            elif nums[mid] > target:
                if mid < lowerOutput:
                    lowerOutput = mid
                return lowerBound(low, mid-1, target, lowerOutput)

            elif nums[mid] == target:
                if mid < lowerOutput:
                    lowerOutput = mid              
                return lowerBound(low, mid, target, lowerOutput)

            return lowerOutput

        return lowerBound(low, high, target, lowerOutput)