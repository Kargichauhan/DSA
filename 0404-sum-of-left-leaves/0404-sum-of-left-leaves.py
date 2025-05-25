# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def process_subtree(subtree,is_left):
            if subtree is None:
                return 0

            if subtree.left is None and subtree.right is None:
                return subtree.val if is_left else 0

            
            return process_subtree(subtree.left, True) + process_subtree(subtree.right,False)

        return process_subtree(root,False)