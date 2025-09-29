class OrderedStream:

    def __init__(self, n: int):
        self.ordered_stream = [0] * n
        self.curr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.ordered_stream[idKey - 1] = value
        data_result = []

        while self.curr < len(self.ordered_stream) and self.ordered_stream[self.curr] != 0:
            data_result.append(self.ordered_stream[self.curr])
            self.curr += 1
        return data_result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
