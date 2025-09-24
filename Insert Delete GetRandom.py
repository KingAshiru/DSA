class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        last_ele = self.array[-1]
        val_idx = self.dict[val]
        self.array[val_idx], self.dict[last_ele] = last_ele, val_idx
        self.array.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return choice(self.array)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
