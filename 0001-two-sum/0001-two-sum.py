class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashing = {}
        for i in range(len(nums)):
            if target - nums[i] in hashing:
                return [hashing[target - nums[i]], i]

            if nums[i] not in hashing:
                hashing[nums[i]] = i
