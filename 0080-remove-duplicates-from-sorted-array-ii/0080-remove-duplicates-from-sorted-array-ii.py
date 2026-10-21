class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        hashing = dict()
        left = 1
        right = 1

        if len(nums) > 0:
            hashing[nums[0]] = 1

        for right in range(1, len(nums)):
            if nums[right] not in hashing:
                hashing[nums[right]] = 1
            elif nums[right] in hashing:
                hashing[nums[right]] += 1

            if hashing[nums[right]] <= 2:
                if left == right:
                    left += 1
                elif left != right:
                    nums[left] = nums[right]
                    left += 1

        return left