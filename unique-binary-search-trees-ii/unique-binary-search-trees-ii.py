# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        
        def DFS(arr):
            if not arr or len(arr) <= 0:
                return [None]
            
            res = []
            for i in range(len(arr)):
                left, right = DFS(arr[:i]), DFS(arr[i + 1:])
                for l in left:
                    for r in right:
                        res.append(TreeNode(arr[i], l, r))
                
            return res
        
        arr = [i for i in range(1, n + 1)]
        return DFS(arr)