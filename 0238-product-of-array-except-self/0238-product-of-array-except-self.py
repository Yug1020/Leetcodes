class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        hasZero = 0
        product = 0
        result = []

        for i in range(len(nums)):
            if nums[i] == 0:
                hasZero += 1
            else:
                if product == 0:
                    product += nums[i]
                else:
                    product *= nums[i]

        for i in range(len(nums)):
            if nums[i] == 0 :
                result.append(product)
            elif hasZero > 1:
                return [0] * len(nums) 
            elif hasZero != 0:
                result.append(0)
            else:
                element = product // nums[i]
                result.append(element)

        return result