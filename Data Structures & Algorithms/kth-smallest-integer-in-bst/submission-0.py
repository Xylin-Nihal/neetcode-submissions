# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        import heapq
        x=[]
        def dfs(root):
            if not root:
                return
            heapq.heappush(x,root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        for i in range(k):
            y=heapq.heappop(x)
        return y