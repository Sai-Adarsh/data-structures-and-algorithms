class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        def backTracking(res, curr_path, count, length, indices):
            if count == length:
                if curr_path not in res:
                    res.append(curr_path)
                return

            for i in range(len(tiles)):
                if i not in indices:
                    backTracking(res, curr_path + tiles[i], count + 1, length, indices + [i])

            return res
        L = []
        for length in range(1, len(tiles) + 1):
            L += backTracking([], "", 0, length, [])
        return len(L)