# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.values = set()

    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.get_nodes(root)
        return len(self.values) == 1

    def get_nodes(self, root):
        self.values.add(root.val)
        if root.left:
            self.get_nodes(root.left)
        if root.right:
            self.get_nodes(root.right)
