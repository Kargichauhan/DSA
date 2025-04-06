# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        U:
        1. binary tree
        2. we collect all leaf nodes -> nodes with no children
        3. then remove those leaves from tree
        4. repeat this till tee is empty
        5. return list of list 


        Example:

        input -> [1,2,3,4,5]

        1 ->2 and 3.. 2-> 4 and 5 

        M: Post order traversal 

        P: 
        1. post order traversal to find the height of each node
        

        I:

        height = 1 + max(left_height, right_height)
        result[height]

        
        res = defaultdict(list)

        def dfs(node):

            if not node:
                return -1 

            left = dfs(node.left)
            right = dfs(node.right)

            height = 1 + max(left,right)

            res[height].append(node.val)

            return height

        dfs(root)
        return [res[i] for i in range(len(res))]
        
        '''

        res = defaultdict(list)

        def dfs(node):

            if not node:
                return -1

            height = 1 + max(dfs(node.left) , dfs(node.right))

            res[height].append(node.val)



            return height

        dfs(root)

        return [res[i] for i in range(len(res))]