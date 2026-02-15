# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(evenParent, addSum, i):
            nonlocal res
            
            if addSum:
                res += i.val

            isEven = i.val % 2 == 0

            if i.left:
                dfs(isEven, evenParent, i.left)
            
            if i.right:
                dfs(isEven, evenParent, i.right)


        dfs(False, False, root)
        return res