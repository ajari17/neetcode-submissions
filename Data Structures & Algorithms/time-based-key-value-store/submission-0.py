class TimeMap:
    def __init__(self):
        self.mapp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapp[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        vals = self.mapp[key]
        print(vals)
        if not vals:
            return ""
        res = ""
        i,j = 0, len(vals) - 1
        while i <= j:
            mid = (i+j) // 2
            if vals[mid][0] <= timestamp:
                res = vals[mid][1]
                i = mid + 1
            else:
                j = mid - 1
        return res



