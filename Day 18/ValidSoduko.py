class Solution:
	# @param A : tuple of strings
	# @return an integer
	def isValidSudoku(self, A):

         for i in range(0,len(A)):
            print(A[i])

        #check for each rule
         res = 1
        #check row wise
         for i in range(0, len(A)):
             hmap = {}
             for j in range(0, len(A[i])):
                if A[i][j] == '.':
                    continue
                elif A[i][j] in hmap:
                    hmap[A[i][j]] += 1
                else:
                    hmap[A[i][j]] = 1
            
             for key in hmap:
                 if hmap[key] >=2:
                     res = 0
                     break

             if res == 0:
                 break
        
        #check column wise
         for j in range(0, len(A[0])):
            hmap = {}
            for i in range(0, len(A)):
                if  A[i][j] == '.':
                    continue
                elif A[i][j] in hmap:
                    hmap[A[i][j]] += 1
                else:
                    hmap[A[i][j]] = 1
           
            for key in hmap:
                if hmap[key] >=2:
                    res = 0
                    break
            if res == 0:
                 break

        #check for each of the 9 subboxes
         for i in range(0,len(A),3):
            hmap = {}
            for j in range(0,len(A[0]),3):

                hmap = {}
                for k in range(i,i+3):
                    for l in range(j,j+3):

                        if  A[k][l] == '.':
                            continue
                        elif A[k][l] in hmap:
                            hmap[A[k][l]] += 1
                        else:
                            hmap[A[k][l]] = 1

                for key in hmap:
                    if hmap[key] >=2:
                        res = 0
                        break

            if res == 0:
                break

         return res

obj = Solution()
A = [ "..4...63.", ".........", "5......9.", "...56....", "4.3.....1", "...7.....", "...5.....", ".........", "........." ]

print(obj.isValidSudoku(A))
            
            

            





