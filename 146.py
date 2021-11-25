class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.order = []
        self.map = {}

    def get(self, key: int) -> int:
        if key in self.map:
            self.order.remove(key)
            self.order.append(key)
            return self.map[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.order.remove(key)
            self.order.append(key)
            self.map[key] = value
        else:
            if len(self.order) == self.capacity:
                del self.map[self.order[0]]
                self.order.pop(0)

            self.order.append(key)
            self.map[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
