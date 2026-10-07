class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def helperFunc(nums, goal):

            if goal < 0:
                return 0

            left = 0
            right = 0
            currSum = 0
            output = 0

            while right < len(nums):
                currSum += nums[right]

                while currSum > goal:
                    currSum -= nums[left]
                    left += 1

                output += right - left + 1

                right += 1

            return output

        # print("goal =", helperFunc(nums, goal))
        # print("goal - 1 =", helperFunc(nums, goal - 1))
        result = helperFunc(nums, goal) - helperFunc(nums, goal - 1)

        return result