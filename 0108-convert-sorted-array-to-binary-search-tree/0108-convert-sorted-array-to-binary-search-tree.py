# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        root_ind = (len(nums) - 1) // 2
        
        def bst(root, left, right):
            left_mid_ind = (len(left) - 1) // 2
            right_mid_ind = (len(right) - 1) // 2
            
            if len(left) != 0:
                left_value = left[left_mid_ind]
            if len(right) != 0:
                right_value = right[right_mid_ind]

            if len(left) != 0:
                root.left = TreeNode(left_value)
                bst(root.left, left[0:left_mid_ind], left[left_mid_ind + 1: len(left)])

            if len(right) != 0:
                root.right = TreeNode(right_value)
                bst(root.right, right[0: right_mid_ind], right[right_mid_ind + 1: len(right)])

            if len(left) == 0 and len(right) == 0:
                return root


        root = TreeNode(nums[root_ind])
        bst(root, nums[0:root_ind], nums[root_ind + 1: len(nums)])

        return root