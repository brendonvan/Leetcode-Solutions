# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        
        def dfs(root):
            if not root:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2 + left + right)
            
            return 1 + max(left, right)
        
#             left = dfs(2) returns 1
#             right = dfs(3) returns 0
#             res[0] = max(res[0], 2 + 1 + 0)
            
#             return 1 + max(left, right)

#             left = dfs(4) returns 0
#             right = dfs(5) returns 0
#             res[0] = max(res[0], 2 + left + right)
            
#             return 1 + max(left, right)
        
        
        #.         1 root
        #.        /.\
        #        2.  3  
        #.      / \.  
        #.     4.  5
        
        
        dfs(root)
        return res[0]
        