# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def ifbst(self, root, minimum, maximum):
        if root is None:
            return True

        #LNR
        if root.val <= minimum:
            return False
        if root.val >= maximum:
            return False
       
        
        leftAns = self.ifbst(root.left, minimum, root.val)
        rightAns = self.ifbst(root.right, root.val, maximum)

        return leftAns and rightAns
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minimum = float('-inf')
        maximum = float('inf')
        return self.ifbst(root, minimum, maximum)
        