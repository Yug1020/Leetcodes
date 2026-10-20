class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        write = 1
        curVal = nums[0]

        for i in range(1, len(nums)):
            # print("nums[i]", nums[i])
            # print("nums[write]", nums[write])
            # print("nums", nums)
            if nums[i] != curVal:
                curVal = nums[i]
                nums[write] = nums[i]
                write += 1
            # print("")
        # print("final", nums)
        return write

        # left = 0
        # output = 0

        # for right in range(1, len(nums)):
        #     if nums[left] == nums[right]:
        #         output += 1
        #     else:
        #         left = right
        # print(output)
        # return output