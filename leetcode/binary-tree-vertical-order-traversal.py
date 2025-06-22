# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        cols = defaultdict(list)
        maxCol = minCol = 0

        queue = deque([(root, 0)])

        while queue:
            node, val = queue.popleft()
            cols[val].append(node.val)
            maxCol, minCol = max(maxCol, val), min(minCol, val)

            if node.left:
                queue.append((node.left, val - 1))
            if node.right:
                queue.append((node.right, val + 1))

        return [cols[c] for c in range(minCol, maxCol + 1)]