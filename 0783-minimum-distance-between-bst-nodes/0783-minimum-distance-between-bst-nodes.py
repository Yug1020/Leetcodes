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
            print("diff", diff)
            print(id(diff))
            if diff[0] == 1:
                print("why not working")
                return diff[0]
            else:
                if current and current.left and diff[0] != 1:
                    sub = float('inf')
                    for i in lastNodes:
                        temp = abs(i - current.left.val)
                        sub = min(sub, temp)
                    # sub = abs(current.val - current.left.val)
                    print("diff btw", current.val ," and", current.left.val ,"is", sub)
                    if sub < diff[0]:
                        diff[0] = sub
                    print("choosen", diff)
                    recMin(current.left, diff, lastNodes)
                if current and current.right and diff[0] != 1:
                    sub = float('inf')
                    for i in lastNodes:
                        temp = abs(i - current.right.val)
                        sub = min(sub, temp)                    
                    # sub = abs(current.val - current.right.val)
                    print("diff btw", current.val ," and", current.right.val ,"is", sub)
                    if sub < diff[0]:
                        diff[0] = sub
                    print("choosen", diff)
                    recMin(current.right, diff, lastNodes)

            return diff[0]

        return recMin(root, [float('inf')], [])
