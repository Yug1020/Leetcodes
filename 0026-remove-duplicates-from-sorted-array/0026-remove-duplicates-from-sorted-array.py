class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        write = 1
        curVal = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != curVal:
                curVal = nums[i]
                nums[write] = nums[i]
                write += 1
        return write