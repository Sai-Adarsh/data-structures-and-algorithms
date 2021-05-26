# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return
        
        span_hash_map = {}
        L = []
        tree = root
        def DFS(root, span):
            if not root:
                return
            if span not in span_hash_map:
                span_hash_map[span] = [root.val]
            else:
                span_hash_map[span].append(root.val)
            L.append(root.val)
            DFS(root.left, span - 1)
            DFS(root.right, span + 1)
            
        DFS(root, 0)
        
        level_hash_map = {None: None}
        tree, root = root, tree
        q = collections.deque([root])
        curr_level = []
        all_levels = []
        
        while q:
            curr_level = []
            for _ in range(len(q)):
                node = q.popleft()
                level_hash_map[node.val] = len(all_levels)
                curr_level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            all_levels.append(curr_level)
            
        
        span_hash_map = list(map(list, span_hash_map.items()))
        span_hash_map.sort(key = lambda x: x[0])
        span_hash_map = [i[1] for i in span_hash_map]
        span_hash_map = [sorted(i, key = lambda x: (level_hash_map[x], x)) for i in span_hash_map]
        return span_hash_map