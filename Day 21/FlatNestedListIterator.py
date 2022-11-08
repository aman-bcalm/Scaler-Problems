class NestedIterator:

    l = None 
    #current element
    ce = 0 
   

    def __init__(self, nestedList):
        self.l = []
        self.ce = 0
        self.makeList(nestedList)
      
    def makeList(self, le):

        for i in range(0, len(le)):
            x = le[i]
            if isinstance(x,list):
               self.makeList(x)
            else:
               self.l.append(x)
               

    def next(self):
    
        self.ce += 1
        return self.l[self.ce-1]
        

    
    def hasNext(self):

        
        if self.ce <= len(self.l)-1:
            return True
        else:
            return False


A =  [1,[4,[6,[5,[[7],13]],[9,[10,[111],11]]]]]
obj = NestedIterator(A)

while obj.hasNext():
    print(obj.next())
