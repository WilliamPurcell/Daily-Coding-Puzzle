# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        answer = self.height(root)
        if answer != -1:
            return True
        return False
        
    def height(self, root):
        if root is None:
            return 0
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        if leftHeight == -1 or rightHeight == -1:
            return -1

        if abs(leftHeight - rightHeight ) > 1:
            return -1

        return 1 + max(leftHeight, rightHeight)