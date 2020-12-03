class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = l = 0
        result = []
        for i in [j for j in s]:
            if i == 'R':
                r += 1
            elif i == 'L':
                l += 1
            if r == l:
                result.append(['R'*r + 'L'*l])
                r = l = 0
        return len(result)
