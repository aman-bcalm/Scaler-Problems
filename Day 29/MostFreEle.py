class Solution:

    def find_most_frequent(self, arr):
    # YOUR CODE GOES HERE
        
        map = {}
        for i in range(0, len(arr)):

            if arr[i] in map:
                map[arr[i]] += 1
            else:
                map[arr[i]] = 1
        
        mx_k = max(map, key = lambda x : map[x])
        return mx_k

    
        #return res


obj = Solution()
a = [2,2,2,1]
obj.find_most_frequent(a)