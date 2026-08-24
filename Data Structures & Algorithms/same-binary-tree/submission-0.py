# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorder(self, root):
        if root is None:
            return [None]
        else:
            return [root.val] + self.preorder(root.left) + self.preorder(root.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # what is i perform some kind of order here

        p_preorder = self.preorder(p)
        q_preorder = self.preorder(q)
        return p_preorder == q_preorder        