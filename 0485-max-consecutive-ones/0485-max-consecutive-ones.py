class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        curr = 0
        large = 0

        for i in nums:
            if i == 1:
                curr += 1
            else:
                if curr > large:
                    large = curr
                curr = 0

        if curr > large:
            large = curr

        return large