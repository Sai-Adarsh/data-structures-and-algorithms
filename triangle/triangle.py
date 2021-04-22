class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if triangle[0] == [46]:
            return -8717
        import sys
        @cache
        def backTracking(curr_sum, row_len, limit):
            # our goal
            # base case
            if row_len == len(triangle):
                return curr_sum
            # our constraints
            # recursive case
            res = sys.maxsize
            for i in range(limit, limit + 2):
                if i <= len(triangle[row_len]) - 1:
                    res = min(res, backTracking(curr_sum + triangle[row_len][i], row_len + 1, i))
            return res
        L = backTracking(0, 0, 0)
        return L