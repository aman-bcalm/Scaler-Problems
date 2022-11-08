

class NestedIterator:
    actual = []
    idx = 0
    n = 0
    def __init__(self, nestedList):
        self.actual = []
        self.rec(nestedList)
        self.n = len(self.actual)
        self.idx = 0
    def rec(self, nestedList):
        for i in range(len(nestedList)):
            x = nestedList[i]
            if(x.isInteger()):
                self.actual.append(x.getInteger())
            else:
                self.rec(x.getList())
    def next(self):
        self.idx += 1
        return self.actual[self.idx-1]
    def hasNext(self):
        if(self.idx < self.n):
            return True
        return False



A =  [1,[4,[6,[5,[[7],13]],[9,[10,[111],11]]]]]
obj = NestedIterator(A)

while obj.hasNext():
    print(obj.next())
