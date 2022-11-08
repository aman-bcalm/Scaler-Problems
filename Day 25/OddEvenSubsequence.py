class Solution:

    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        #index of first even and first odd no
        i_a = []
        fi = False
        fo = False
        for i in range(0, len(A)):

            if A[i] % 2 == 0 and not fi :
                i_a.append(i)
                fi = True
            
            if A[i] % 2 != 0 and not fo :
                i_a.append(i)
                fo = True

            if fi and fo:
                break

        

        m_l = 0
        for i in i_a:

            nOdd = False
            nEven = False
            l = 0
            for j in range(i, len(A)):

                if j == i:

                    if A[j] % 2 == 0:
                        nOdd = True
                    else:
                        nEven = True
                    l += 1   
                else:

                    if nOdd and A[j] % 2 != 0:
                        l += 1
                        nOdd = False
                        nEven = True
                    
                    if nEven and A[j] % 2 == 0:
                        l += 1
                        nOdd = True
                        nEven = False
            
            if l >= m_l:
                m_l = l
        
        return m_l

obj = Solution()
A = [2,2,2,2]
print(obj.solve(A))



                    

