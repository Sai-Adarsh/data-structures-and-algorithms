class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        def dfs(x, y):
            if board[x][y] == 'M': board[x][y] = 'X'
            elif board[x][y] == 'E':
                cnt, nei = 0, []
                for i, j in map(lambda v: (v[0]+x, v[1]+y), [(-1, 0), (1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 1)]):
                    if 0 <= i < m and 0 <= j < n:
                        nei.append((i, j))
                        if board[i][j] == 'M': cnt += 1
                if not cnt:
                    board[x][y] = 'B'
                    for i, j in nei: dfs(i, j)
                else: board[x][y] = str(cnt)
        
        x, y = click
        dfs(x, y)            
        return board