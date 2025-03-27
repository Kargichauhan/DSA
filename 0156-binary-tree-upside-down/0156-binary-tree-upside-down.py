# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #dfs

        if not root:
            return None

        if not root.left and not root.right:
            return root

        newroot = self.upsideDownBinaryTree(root.left)

        root.left.left = root.right
        root.left.right = root

        root.left = None
        root.right = None

        return newroot



        #o(n) -tc
        #o(n)- sc



        
        