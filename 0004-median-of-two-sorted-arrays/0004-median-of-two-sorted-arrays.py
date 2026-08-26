class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        plus = n1 + n2
        arrIs = "even"
        print("plus", plus)

        if plus % 2 == 0:
            arrIs = "even"
        else:
            arrIs = "odd"
        print("arrIs", arrIs)

        if arrIs == "even":
            ind = plus / 2
        else:
            ind = plus // 2
        print("ind", ind)

        if arrIs == "odd":
            for _ in range(ind):
                if len(nums1)!=0 and len(nums2)!= 0 and nums1[0] <= nums2[0]:
                    nums1.pop(0)
                elif len(nums1)!=0 and len(nums2)!= 0 and nums1[0] >= nums2[0]:
                    nums2.pop(0)
                elif len(nums1) == 0:
                    nums2.pop(0)
                elif len(nums2) == 0:
                    nums1.pop(0)

            if len(nums1)!=0 and len(nums2)!= 0 and nums1[0] <= nums2[0]:
                return nums1.pop(0)
            elif len(nums1)!=0 and len(nums2)!= 0 and nums1[0] >= nums2[0]:
                return nums2.pop(0)
            elif len(nums1) == 0:
                return nums2.pop(0)
            elif len(nums2) == 0:
                return nums1.pop(0)

        if arrIs == "even":
            for _ in range(int(ind)):
                if len(nums1)!=0 and len(nums2)!= 0 and nums1[0] <= nums2[0]:
                    last_value = nums1.pop(0)
                elif len(nums1)!=0 and len(nums2)!= 0 and nums1[0] >= nums2[0]:
                    last_value = nums2.pop(0)
                elif len(nums1) == 0:
                    last_value = nums2.pop(0)
                elif len(nums2) == 0:
                    last_value = nums1.pop(0)

            if len(nums1)!=0 and len(nums2)!= 0 and nums1[0] <= nums2[0] :
                res = (nums1[0] + last_value) / 2
                return res

            elif len(nums1)!=0 and len(nums2)!= 0 and nums1[0] >= nums2[0]:
                res = (nums2[0] + last_value) / 2
                return res

            elif len(nums1) == 0:
                res = (nums2[0] + last_value) / 2
                return res

            elif len(nums2) == 0:
                res = (nums1[0] + last_value) / 2
                return res
