class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return 2
        min_num = float("inf")
        min_ind = 1

        max_num = float("-inf")
        max_ind = 1

        result_dic = {}
        for i in range(len(nums)):
            if nums[i] <= min_num:
                min_num = nums[i]
                min_ind = i

            if nums[i] >= max_num:
                max_num = nums[i]
                max_ind = i
        
        print("min_ind:-", min_ind, "max_ind:-", max_ind)
        min_fL = abs(min_ind + 1)
        min_fR = abs(len(nums) - min_ind)

        # print("min_fL", min_fL, "min_fR", min_fR)

        Final_min_ind = min(min_fL, min_fR)

        max_fL = abs(0 - (max_ind + 1))
        max_fR = abs(len(nums) - max_ind)

        # print("max_fL", max_fL, "max_fR",max_fR)
        Final_max_ind = min(max_fL, max_fR)

        result_L = max(min_ind, max_ind) + 1
        result_R = len(nums) - (min(min_ind, max_ind))


        addition = Final_min_ind + Final_max_ind
        print(addition, result_R, result_L)
        result = min(addition, result_R, result_L)
        return result
