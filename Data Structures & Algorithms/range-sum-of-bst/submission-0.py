# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, low, high, range_sum):
        if root is None:
            return range_sum
        if root.val<=high and root.val>=low:
            range_sum+=root.val
        
        left_sum = self.solve(root.left, low, high, range_sum)
        
        right_sum = self.solve(root.right, low, high, range_sum)
        
        return left_sum + right_sum-range_sum
        
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        range_sum = 0

        return self.solve(root, low, high, range_sum)  

             