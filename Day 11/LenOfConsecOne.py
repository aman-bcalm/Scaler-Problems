class Solution:

    #approach consists of prefix sum left and prefix sum right array n counting total no of 1s


    # @param A : string
    # @return an integer
    def solve(self, A):

        count1s = 0
        left_sum = [0] * len(A)
        for i in range(0 , len(A)):

            if i == 0 and A[i] == '1':
                left_sum[i] = 1
                count1s += 1
            elif A[i] == '0':
                left_sum[i] = 0
            elif A[i] == '1':
                left_sum[i] = left_sum[i-1] + 1
                count1s += 1
        
        
       

        right_sum = [0] * len(A)
        for i in range(len(A)-1,-1,-1):

            if i == len(A)-1 and A[i] == '1':
                right_sum[i] = 1
            elif A[i] == '0':
                right_sum[i] = 0
            elif A[i] == '1':
                right_sum[i] = right_sum[i+1] + 1
        
       
        res = max(max(left_sum), max(right_sum))
        for i in range(1, len(A)-1):

            if A[i] == '0' and  i == 0:

                if len(A) >=2 and count1s - right_sum[i+1] >= 1:
                    res_i = right_sum[i+1] + 1
                    res = max(res,res_i)
                else: #length is 1
                    res = count1s

            elif A[i] == '0' and  i == len(A)-1:

                if count1s - left_sum[i-1] >= 1:
                    res_i = left_sum[i-1] + 1
                    res = max(res,res_i)
    

            elif A[i] == '0' and (count1s - left_sum[i-1] - right_sum[i+1])  >= 0:
                #print(i, left_sum[i-1], right_sum[i+1])
                if count1s  - left_sum[i-1] - right_sum[i+1] >=1 :
                    res_i = left_sum[i-1] + right_sum[i+1] + 1
                    
                elif count1s  - left_sum[i-1] - right_sum[i+1] >=0: 
                    res_i = left_sum[i-1] + right_sum[i+1] 
                
                res = max(res,res_i)

        return res


obj = Solution()
A = "111011101"
print(obj.solve(A))
        

                
                    
        

        



        
    
                    
                






    


        

