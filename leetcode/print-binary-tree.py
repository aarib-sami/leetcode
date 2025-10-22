# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        height = self.calculateHeight(root)
        n = (2**(height)) - 1
        m = height + 1
        res = [[""]*n for _ in range(height)]
        l = 0
        r = n
        
        def helper(root, rowNum, l, r):
            if not root:
                return

            mid = (l + r) // 2
            res[rowNum][mid] = str(root.val)

            helper(root.left, rowNum+1, l, mid-1)
            helper(root.right, rowNum+1, mid+1, r)

        helper(root, 0, l, r)
        return res

    def calculateHeight(self, root):
            height = 0
            q = deque([root])

            while q:
                length = len(q)
                for i in range(len(q)):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                height += 1

            return height