class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board),len(board[0])
        path = set()
        def search(i,r,c):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r,c) in path):
                return False
            path.add((r,c))
            res = (search(i+1,r+1,c) or 
                    search(i+1,r-1,c) or 
                    search(i+1,r,c-1) or 
                    search(i+1,r,c+1))
            path.remove((r,c))
            return res
        for r in range(rows):
            for c in range(cols):
                if search(0,r,c): return True
        return False

        