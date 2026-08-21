class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # arr = []
        hashmap = {}
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] = True
            else:
                hashmap[nums[i]] = False
        
        for key, value in hashmap.items():
            if value is False:
                return key
                