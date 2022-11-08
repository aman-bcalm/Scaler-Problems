class Solution:

    def invert_dict(self ,data):
    # YOUR CODE GOES HERE
     data1 = {}
     for k in data.keys():

         data1[data[k]] = k
         #del data[k]

     return data1




obj = Solution()
data =  {'a': 1, 'b':2}
print(obj.invert_dict(data))