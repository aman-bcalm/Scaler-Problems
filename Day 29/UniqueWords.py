class Solution:

    def count_unique_words(self,arr):
    # YOUR CODE GOES HERE
     
     res = 0
     for i in range(0, len(arr)):
         if len(arr[i]) > 3:
              
              mp = {}
              for j in range(0, len(arr[i])):
                  if arr[i][j] in mp:
                      mp[arr[i][j]] += 1
                  else:
                      mp[arr[i][j]] = 1
              #print(mp)
              uni = True
              for x in  mp.values():
                  if x > 1:
                      uni = False
                      break
                      
              if uni:
                 res += 1
     return res




obj = Solution()
a = ["grapes", "help", "apple", "orange", "was", "hello"]
print(obj.count_unique_words(a))

