# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        if not root:
            return
        self.L = []
        def DFS(root):
            if not root:
                return
            DFS(root.left)
            self.L.append(root.val)
            DFS(root.right)
        DFS(root)

        self.count = 0
    def next(self) -> int:
        if self.count <= len(self.L):
            temp = self.count
            self.count += 1
            return self.L[temp]
        
    def hasNext(self) -> bool:
        if self.count >= len(self.L):
            return False
        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()