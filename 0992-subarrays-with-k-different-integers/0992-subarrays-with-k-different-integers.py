class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def helperFunc(nums, k):
            if k < 0:
                return 0

            left = 0
            hashing = {}
            max_len = 0

            for right in range(len(nums)):
                if nums[right] not in hashing:
                    hashing[nums[right]] = 1
                else:
                    hashing[nums[right]] += 1

                while len(hashing) > k:
                    hashing[nums[left]] -= 1
                    if hashing[nums[left]] == 0:
                        del hashing[nums[left]]
                    left += 1

                max_len += right - left + 1

            return max_len

        return (helperFunc(nums, k) - helperFunc(nums, k - 1))