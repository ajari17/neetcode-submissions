class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # maps key -> Node

        # Dummy boundary nodes:
        # left.next points to the LRU node
        # right.prev points to the MRU node
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # Remove node from doubly linked list
    def remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Insert node at right (Most Recently Used)
    def insert(self, node: Node) -> None:
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            # Move accessed node to the right (MRU)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        # Create and insert new node at MRU
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # Evict LRU if capacity exceeded
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]