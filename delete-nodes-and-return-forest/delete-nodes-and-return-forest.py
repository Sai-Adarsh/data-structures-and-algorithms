# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        trees = []
        target = set(to_delete)
        
        def DFS(root):
            if not root:
                return
            root.left = DFS(root.left)
            root.right = DFS(root.right)
            if root.val not in target:
                return root
            else:
                if root.left:
                    trees.append(root.left)
                if root.right:
                    trees.append(root.right)
            
        dummy_tree = TreeNode(to_delete[0], left = root)
        DFS(dummy_tree)
        return trees