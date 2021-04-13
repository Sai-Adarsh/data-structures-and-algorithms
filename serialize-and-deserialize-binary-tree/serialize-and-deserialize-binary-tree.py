# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return
        self.L = []
        def DFS(root):
            if not root:
                self.L.append("N")
                return
            self.L.append(str(root.val))
            DFS(root.left)
            DFS(root.right)
        DFS(root)
        return ", ".join(self.L)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.L = data
        if not self.L:
            return
        self.L = self.L.split(", ")
        
        def DFS():
            if self.L[self.curr_pos] == "N":
                self.curr_pos += 1
                return
            root = TreeNode(int(self.L[self.curr_pos]))
            self.curr_pos += 1
            root.left = DFS()
            root.right = DFS()
            return root
        self.curr_pos = 0
        return DFS()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))