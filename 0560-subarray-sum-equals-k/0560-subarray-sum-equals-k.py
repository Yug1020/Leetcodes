class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        hashing = {0: 1}
        count = 0

        for i in range(len(nums)):
            prefixSum += nums[i]

            if prefixSum - k in hashing:
                count += hashing[prefixSum - k]

            if prefixSum not in hashing:
                hashing[prefixSum] = 1
            elif prefixSum in hashing:
                hashing[prefixSum] += 1

        return count

# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         prefixSum = 0
#         hashing = {0:1}
#         count = 0

#         for i in range(len(nums)):
#             prefixSum += nums[i]
            
#             if prefixSum - k in hashing:
#                 count += hashing[prefixSum-k]
            
#             hashing[prefixSum] = 1 + hashing.get(prefixSum, 0)
        
#         return count