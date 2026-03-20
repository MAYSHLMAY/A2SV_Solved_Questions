# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.final = []

    def dfs(self, node):
        if not node: return
        self.dfs(node.left)
        self.final.append(node.val)
        self.dfs(node.right)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # self.final = []
        self.dfs(root)
        return self.final