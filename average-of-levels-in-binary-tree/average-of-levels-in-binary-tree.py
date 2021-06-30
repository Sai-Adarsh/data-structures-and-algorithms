# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return
        
        q = collections.deque([root])
        curr_level = []
        all_levels = []
        
        while q:
            curr_level = []
            for _ in range(len(q)):
                node = q.popleft()
                bisect.insort(curr_level, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            all_levels.append(sum(curr_level) / len(curr_level))
        return all_levels
                