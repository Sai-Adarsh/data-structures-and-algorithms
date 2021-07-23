# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        # level order traversal and find max, return max
        if not root:
            return
        q = collections.deque([root])
        curr_level = 0
        all_levels = -sys.maxsize - 1
        level = 1
        count = 1
        
        while q:
            curr_level = 0
            for _ in range(len(q)):
                node = q.popleft()
                curr_level += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if curr_level > all_levels:
                all_levels = curr_level
                level = count
                
            count += 1
        return level