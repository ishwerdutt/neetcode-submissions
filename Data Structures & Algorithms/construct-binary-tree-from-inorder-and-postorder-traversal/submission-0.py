# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

   
    
    def build(self, inorder, postorder, postorder_ind, start_ind, end_ind):
        if self.postorder_ind < 0:
            return None
        if start_ind > end_ind:
            return None
        
        element = postorder[self.postorder_ind]
        self.postorder_ind = self.postorder_ind - 1
        element_ind_in_inorder = self.inorder_map[element]
        root = TreeNode(element)

        

        root.right = self.build(inorder,
                                postorder,
                                self.postorder_ind,
                                element_ind_in_inorder+1,
                                end_ind)
        

        root.left = self.build(inorder,
                                postorder,
                                self.postorder_ind,
                                start_ind,
                                element_ind_in_inorder-1)
        
        
        
        return root
        
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.postorder_ind = len(postorder) - 1
        start_ind = 0
        end_ind = len(inorder) - 1
        self.inorder_map = {
                            value: i
                            for i, value in enumerate(inorder)
                            }
        root = TreeNode()
        root = self.build(inorder,
                    postorder,
                    self.postorder_ind,
                    start_ind,
                    end_ind)
        return root
        