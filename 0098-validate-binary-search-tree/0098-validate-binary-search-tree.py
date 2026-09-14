# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []

        def fun(root):
            if root and root.left :
                fun(root.left)
            if root is not None:
                result.append(root.val)
            if root and root.right:
                fun(root.right)
        fun(root)

        for i in range(len(result) - 1):
            nxt_ind = i + 1
            if result[i] < result[nxt_ind]:
                pass
            else:
                return False
        return True