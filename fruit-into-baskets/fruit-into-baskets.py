class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        
        
        two_dict = {}
        left = 0
        right = 0
        m = 0
        while right < len(tree):
            two_dict[tree[right]] = tree[right]
            if len(two_dict) > 2:
                m = max(m, right - left)
                right -= 1
                two_dict = {}
                left = right
                while tree[left - 1] == tree[right]:
                    left -= 1
            else:
                right += 1
        m = max(m, right - left)
        return (m)