class Solution:
    def exist(self, board, word):
        visited = set()
        m, n = len(board), len(board[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, i):
            if i >= (len(word)):
                return True
            # invalid conditions
            if min(r, c) < 0 or r >= m or c >= n or (r, c) in visited or board[r][c] != word[i]:
                return False

            visited.add((r, c))

            for dr, dc in dirs:
                if dfs(r + dr, c + dc, i + 1):
                    return True

            visited.remove((r, c))

            return False

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True

        return False