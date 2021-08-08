# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def maxDepthHelper(tree):
            if tree is None:
                return 0
            if tree.left is None and tree.right is None:
                return 1
            else:
                return max(maxDepthHelper(tree.left), maxDepthHelper(tree.right))+1
        return maxDepthHelper(root)
