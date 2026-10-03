class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        curr_len = 0
        max_len = 0
        l = 0
        r = 0

        while r < len(nums):
            if nums[r] == 1 and curr_len == 0:
                l = r

            if nums[r] == 1 and nums[l] == 1:
                curr_len = r - l + 1
                max_len = max(max_len, curr_len)
            
            if nums[r] == 0:
                curr_len = 0
                l = r
            
            r += 1

        return max_len