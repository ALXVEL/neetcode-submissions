# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def balance(root):
            if not root:
                return 0

            leftHeight = balance(root.left)
            rightHeight = balance(root.right)

            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            
            return 1 + max(leftHeight, rightHeight)
        
        
        if balance(root) == -1:
            return False
        else:
            return True