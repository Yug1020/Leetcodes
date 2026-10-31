class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums

        r0 = 0
        r1 = 0
        r2 = len(nums) - 1

        while r1 <= r2:
            if r1 <= r2 and nums[r1] == 2:
                nums[r1], nums[r2] = nums[r2], nums[r1]
                while nums[r2] == 2 and r2 >= r1:
                    r2 -= 1
            
            if r0 == r1 and r1 <= r2 and nums[r1] == 0:
                r0 += 1
                r1 += 1
            
            if r0 != r1 and r1 <= r2 and nums[r1] == 0:
                nums[r0], nums[r1] = nums[r1], nums[r0]
                r0 += 1
                r1 += 1
            
            if r1 <= r2 and nums[r1] == 1:
                r1 += 1
