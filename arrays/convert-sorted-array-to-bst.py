# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def subTree(self, nums, start, end):
        if start>end:
            # invalid index
            return None
        mid = (start+end)//2
        root = TreeNode(nums[mid])
        root.left = self.subTree(nums, start, mid-1)
        root.right = self.subTree(nums, mid+1, end)
        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.subTree(nums, 0, len(nums)-1)