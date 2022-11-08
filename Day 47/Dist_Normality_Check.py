import numpy as np

class Solution:

    def normality_test(self , arr):
        '''
        Input: 
        arr: a python list denoting the input distribution of floating point values
        Output:
        res: return "yes" or "no" as per required, of type string
        '''
        S = 0
        for i in range(0, len(arr)):
            S += arr[i]
        
        m = S / len(arr)

        S1 = 0
        for i in range(0, len(arr)):
            t = arr[i] - m
            t =  t * t
            S1 += t
        
        S1 = S1 / len(arr)

        # mean is m and st is standard devaition
        st = S1 ** (1/2)


        res = "yes"
        c1 = 0
        #fist standard deviation
        for i in range(0, len(arr)):

            if (m-st) <= arr[i] <= (m+st):
                c1 += 1
        
        if not (0.66 <= (c1/len(arr)) <= 0.7) :
            res = "no"
            return res
        

         #second standard deviation
        c2 = 0
       
        for i in range(0, len(arr)):

            if (m- (2* st)) <= arr[i] <= (m+ (2 *st)):
                c2 += 1

        if not(0.93 <= (c2/len(arr)) <= 0.97) :
            res = "no"
            return res

        #third standard devaition
        c3 = 0 

        for i in range(0, len(arr)):

            if (m- (3* st)) <= arr[i] <= (m+ (3 *st)):
                c3 += 1

        if not(0.977 <= (c3/len(arr)) <= 1) :
            res = "no"
            return res




        
        # Your code goes here
        
        
        # Your code ends here
        return res


obj = Solution()
data =  [0.44122748688504143, -0.33087015189408764, 2.43077118700778, -0.2520921296030769, 0.10960984157818278, 1.5824811170615634, -0.9092324048562419, -0.5916366579302884, 0.18760322583703548, -0.32986995777935924 ]
print(obj.normality_test(data))

