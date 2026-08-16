class Node:
    def __init__(self):
        self.children = {}
        self.isLast = False
class Solution:
    def __init__(self):
        self.root = Node()
    def add_words(self, words):
        for word in words:
            cur = self.root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = Node()
                cur = cur.children[char]
            cur.isLast = True
                    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.add_words(words)
        ROWS,COLS = len(board), len(board[0])
        res,visit = set(),set()
        def dfs(r,c,node,cur_wrd):
            #base case
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visit or board[r][c] not in node.children:                return
            visit.add((r,c))
            node = node.children[board[r][c]]
            cur_wrd += board[r][c]
            if node.isLast:
                res.add(cur_wrd)
            dfs(r+1,c,node,cur_wrd)
            dfs(r-1,c,node,cur_wrd)
            dfs(r,c+1,node,cur_wrd)
            dfs(r,c-1,node,cur_wrd)
            visit.remove((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,self.root,"")
        return list(res)
