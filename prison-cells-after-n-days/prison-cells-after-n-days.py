class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        copy = []
        N = (N - 1) % 14 + 1
        for _ in range(N):
            copy[:] = cells
            copy[0], copy[-1] = 0, 0
            for j in range(1, len(cells) - 1):
                if cells[j - 1] == cells[j + 1]:
                    copy[j] = 1
                else:
                    copy[j] = 0
            cells[:] = copy
        return cells
