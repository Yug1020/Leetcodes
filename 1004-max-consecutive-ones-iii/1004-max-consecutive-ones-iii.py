class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        curr = 0
        large = 0
        
        l = 0
        # r = 0

        zeros = 0

        # while r < len(nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1

            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            
            curr = i - l + 1
            if curr > large:
                large = curr
            
            # r += 1
        
        return large