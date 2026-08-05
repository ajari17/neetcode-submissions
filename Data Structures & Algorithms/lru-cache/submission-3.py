class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        temp = None
        for mapp in self.cache:
            if key in mapp.keys():
                temp = mapp
                self.cache.pop(self.cache.index(mapp))
                self.cache.append(temp)
                return mapp[key]
        return -1

    def put(self, key: int, value: int) -> None:
        for mapp in self.cache:
            if key in mapp.keys():
                self.cache.pop(self.cache.index(mapp))
        self.cache.append({key:value})
        if len(self.cache) > self.capacity:
            self.cache.pop(0)
    
        
