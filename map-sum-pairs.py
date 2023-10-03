class MapSum:

    def __init__(self):
        self.map = {}
        

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        count = 0
        for key,val in self.map.items():
            if key[:len(prefix)] == prefix:
                count += val

        return count

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)