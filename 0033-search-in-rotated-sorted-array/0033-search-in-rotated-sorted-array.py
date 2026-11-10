class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        output = -1


        def recursion(low, high, nums, target, output):
            if low > high:
                return output

            mid = (low + high) // 2

            if nums[mid] == target:
                output = mid 
                return output
            
            if nums[low] == target:
                output = low 
                return output
            
            if nums[high] == target:
                output = high 
                return output
            
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    return recursion(low, mid - 1, nums, target, output)
                else:
                    return recursion(mid + 1, high, nums, target, output)
                
            elif nums[mid] <= nums[high]:
                if nums[mid] <= target <= nums[high]:
                    return recursion(mid + 1, high, nums, target, output)
                else:
                    return recursion(low, mid - 1, nums, target, output)

            return -1
        
        return recursion(low, high, nums, target, output)
