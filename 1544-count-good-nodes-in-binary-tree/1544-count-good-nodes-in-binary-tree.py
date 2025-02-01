# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #dfs
        count = 0 
        def dfs(tree, maxim):
            nonlocal count

            if not tree: return


            if tree.val >= maxim:
                maxim = tree.val
                count += 1

            dfs(tree.left, maxim)
            dfs(tree.right, maxim)
        dfs(root, root.val)
        return count


        
        