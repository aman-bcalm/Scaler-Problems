class Solution:

    def revst(self, i, j, A):

        while i < j:
           temp =  A[i]
           A[i] = A[j]
           A[j] = temp
           i += 1
           j -= 1
        
        


    # @param A : string
    # @return a strings
    def solve(self, A): 
        A = A.strip()
        A = list(A)
        self.revst(0, len(A)-1,A)
        
        start = 0
        for i in range(0, len(A)):

            if A[i] == ' ':
                self.revst(start,i-1,A)
                start = i + 1
            
            
            if i == len(A) - 1:
                self.revst(start,i,A)
        A = ''.join(A)
        return A

        
       


obj = Solution()
A = "crulgzfkif gg ombt vemmoxrgf qoddptokkz op xdq hv "
print(obj.solve(A))



