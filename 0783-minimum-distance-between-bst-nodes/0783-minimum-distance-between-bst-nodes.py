# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:
        def recMin(current, diff, lastNodes):
            lastNodes.append(current.val)
            if diff[0] == 1:
                return diff[0]
                
            sub = float('inf')
            if current and current.left and diff[0] != 1:
                for i in lastNodes:
                    temp = abs(i - current.left.val)
                    sub = min(sub, temp)
                if sub < diff[0]:
                    diff[0] = sub
                recMin(current.left, diff, lastNodes)
            if current and current.right and diff[0] != 1:
                for i in lastNodes:
                    temp = abs(i - current.right.val)
                    sub = min(sub, temp)                    
                if sub < diff[0]:
                    diff[0] = sub
                recMin(current.right, diff, lastNodes)

            return diff[0]

        return recMin(root, [float('inf')], [])
