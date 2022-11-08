import math
from itertools import chain, combinations

class Solution:

    def powerset(self, s):
        return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))


    # @param A : integer
    # @return an integer
    def solve(self,A):

        res = [int(math.pow(5,1))]
        pwr = 2
        ans = -1


        while 1:

            res.append(int(math.pow(5,pwr)))
            
            subsets = list(self.powerset(res))
            
            
           
            for i in range(0, len(subsets)) :
                S = 0
                for j in range(0, len(subsets[i])):
                    S += subsets[i][j]
                subsets [i] = S
            
            subsets = list(dict.fromkeys(subsets))
            subsets.sort()
            if A > len(subsets):
                pwr += 1
            else:
                ans = subsets[A-1]
                break
            
        print(ans,A,subsets)
        return ans 




        


obj = Solution()
A = 10
#t = [5,25,125,625]
#print(list(obj.powerset(t)))
#print(len(list(obj.powerset(t))))
print(obj.solve(A))