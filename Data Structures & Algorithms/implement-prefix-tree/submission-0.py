class Node:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class PrefixTree:
    def __init__(self):
        self.root = Node()
    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children: 
                cur.children[char] = Node()#if a new alphabet is found add it
            cur = cur.children[char]#move to next char

        cur.end_of_word = True#at the last word the word is obv over so u mark it with true

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.children:#if cur is last word and last word is marked true
                return False
            cur = cur.children[char]#move cur forward
        return cur.end_of_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True

        
        