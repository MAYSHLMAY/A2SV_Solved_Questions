# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return [] 

        q = deque([root])
        s = [root]

        ltr = True
        final = []

        # whenever 2 elements 
        # out from the queue 4 elements join 
        # and continues like that

        while q:
            temp = deque()

            for _ in range(len(q)):
                front = q.popleft()

                if ltr: temp.append(front.val)
                else: temp.appendleft(front.val)

                if front.left:
                    q.append(front.left)
                if front.right:
                    q.append(front.right)

            final.append(list(temp))
            ltr = not ltr
        return final