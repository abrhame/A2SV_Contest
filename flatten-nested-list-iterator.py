class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.list = []
        self.flatten(nestedList)

    def flatten(self, nestedList):
        for item in nestedList:
            if item.isInteger():
                self.list.append(item.getInteger())
            else:
                self.flatten(item.getList())

    def next(self) -> int:
        if self.hasNext():
            val = self.list[0]
            self.list = self.list[1:]
            return val

    def hasNext(self) -> bool:
        return len(self.list) > 0