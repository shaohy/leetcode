# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.build_BST(nums, 0, len(nums))

    def build_BST(self, nums: List[int], l: int, r: int) -> TreeNode:
        if r - l <= 0:
            return None
        if r - l == 1:
            return TreeNode(nums[l])

        mid_idx = l + (r - l) // 2
        root = TreeNode(nums[mid_idx])
        root.left = self.build_BST(nums, l, mid_idx)
        root.right = self.build_BST(nums, mid_idx + 1, r)

        return root