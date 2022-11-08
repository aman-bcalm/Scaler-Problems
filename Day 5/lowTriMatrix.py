class lowTriMatrix :
     # @param A : tuple of list of integers
    # @return an integer
    def solve(self, A):

        answer = 1
        for i in range (0, len(A)) :
            for j in range (i+1, len(A[i])) :
                if A[i][j] != 0 :
                    answer=0
                    break
            
            if answer == 0:
                break
        
        return answer


obj = lowTriMatrix()
t_val = ([1,0,0], [0,0,0], [-7,-8,9])
print(obj.solve(t_val))
t_val1 = ([285, -982],[931, -482])
print(obj.solve(t_val1))
