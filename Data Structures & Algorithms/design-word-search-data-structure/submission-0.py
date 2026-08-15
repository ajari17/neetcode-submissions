class Node:
    def __init__(self):
        self.children = {}
        self.last = False
class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()
            cur = cur.children[char]
        cur.last = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j,len(word)):
                char = word[i]
                if char == ".":
                    for child in cur.children.values():
                        if dfs(i+1,child): 
                            return True
                    return False
                else:
                    if char not in cur.children:
                        return False
                    else:
                        cur = cur.children[char]
            return cur.last
        return dfs(0,self.root)

         
