class Solution:

    def solve(self, A):
        #no fo doors = no of monkeys = A
        l = []
        for i in range(0,A+1):
            l.append(0)
        #all doors are closed

        #monkey no i
        for i in range (1,A+1):
         for j in range(1,A+1):

            if j % i == 0:
                if l[j] == 0:
                    l[j] = 1
                else:
                    l[j] = 0
        
       
        c = 0
        for i in range(1,A+1):
            if l[i] == 1:
                c += 1
        print(c)



obj = Solution()
A = 100
obj.solve(A)