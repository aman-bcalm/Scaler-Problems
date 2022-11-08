class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        ans = []
        for i in range(0,len(A)):
            tc = A[i]
            if i == len(A)-1:
                ans.append(tc)
                break
            else:
                cond = 1
                for j in range(i+1,len(A)):
                    if A[j] > tc:
                        cond = 0
                        break
                if cond == 1:
                    ans.append(tc)
        return ans

