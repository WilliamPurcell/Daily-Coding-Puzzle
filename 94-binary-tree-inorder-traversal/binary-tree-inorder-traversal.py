# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        Output = []
        self.inorderRecurs(root, Output)
        return Output
    
    def inorderRecurs(self, node, result):
        if node != None:
            # Left
            self.inorderRecurs(node.left, result)
            # Root
            result.append(node.val)
            # Right
            self.inorderRecurs(node.right, result)

        