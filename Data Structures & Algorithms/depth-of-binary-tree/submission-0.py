# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def depth(root, current_depth):
            
            if not root:
                return current_depth

            left_depth = depth(root.left, current_depth + 1)
            right_depth = depth(root.right, current_depth + 1)

            return max(left_depth, right_depth)
        
        return depth(root, 0)
