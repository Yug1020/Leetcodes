class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        new_nums = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                new_nums.append(0)
            else:
                new_nums.append(1)

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

        return (helperFunc(new_nums, k) - helperFunc(new_nums, k - 1))


        # def helperFunc(nums, goal):
        #     if goal < 0:
        #         return 0

        #     left = 0
        #     oddCount = 0
        #     output = 0

        #     for right in range(len(nums)):

        #         if nums[right] % 2 == 1:
        #             oddCount += 1

        #         while oddCount > goal:
        #             oddCount -= 1
        #             left += 1

        #         output += right - left
        #         print("right", right)
        #         print("nums[right]", nums[right])
        #         print("oddCount", oddCount)
        #         print("")
        #     if left == 0:

        #     return output

        # print("k", helperFunc(nums, k))
        # print("k - 1", helperFunc(nums, k - 1))  
        # return (helperFunc(nums, k) - helperFunc(nums, k - 1))
