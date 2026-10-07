class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def helperFunc(nums, goal):

            if goal < 0:
                return 0

            left = 0
            currSum = 0
            output = 0

            for right in range(len(nums)):
                currSum += nums[right]

                while currSum > goal:
                    currSum -= nums[left]
                    left += 1

                output += right - left + 1

            return output

        # result = (helperFunc(nums, goal) - helperFunc(nums, goal - 1))

        return (helperFunc(nums, goal) - helperFunc(nums, goal - 1))