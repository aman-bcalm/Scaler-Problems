class MinStack:

    li = None
    li_min = None
   
  
    
    def __init__(self):
        self.li = []
        self.li_min = []
        
    

    # @param x, an integer
    # @return an integer
    def push(self, x):

        if len(self.li) == 0:
            self.li.append(x)
            self.li_min.append(x)
            
        else:
            if x <= self.li_min[-1] :
                self.li_min.append(x)
               

            self.li.append(x)    

        

    # @return nothing
    def pop(self):
        if len(self.li_min) == 0:
            return 
        else:
            #we've encountered a minimum element, pop both normal and min stack
            if self.li[-1] == self.li_min[-1]:
                res = self.li.pop()
                self.li_min.pop()

                return res
            #not a minimum element just pop normal stack
            else:
                res = self.li.pop()
                return res

    # @return an integer
    def top(self):
        if len(self.li) == 0:
            return -1
        else:
            return self.li[-1]
        

    # @return an integer
    def getMin(self):
        if len(self.li_min) == 0:
            return -1
        else :
            return self.li_min[-1]


obj = MinStack()
print(obj.getMin())
print(obj.pop())
print(obj.top())
        
