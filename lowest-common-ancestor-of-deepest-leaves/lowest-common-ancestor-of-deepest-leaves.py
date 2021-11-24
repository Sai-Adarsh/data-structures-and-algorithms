# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def addParent(root, parent):
            if not root:
                return
            root.parent = parent
            addParent(root.left, root)
            addParent(root.right, root)
            return root
        
        root = addParent(root, None)
        
        
        # level order to find the deepest
        q = collections.deque([root])
        currLevel = []
        allLevels = []
        
        while q:
            currLevel = []
            for _ in range(len(q)):
                node = q.popleft()
                currLevel.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            allLevels.append(currLevel)
            
        temp = allLevels[-1]
        
        if len(temp) == 1:
            return temp[-1]
        else:
            
            self.hashMap = collections.Counter()
            self.ans = None
            def DFS(root):
                if not root:
                    return
                self.hashMap[root] += 1
                if self.hashMap[root] == len(temp):
                    self.ans = root
                    return
                DFS(root.parent)
                
            for eachRoot in temp:
                DFS(eachRoot)
                if self.ans:
                    return self.ans