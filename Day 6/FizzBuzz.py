class Solution:
	# @param A : integer
	# @return a list of strings
	def fizzBuzz(self, A):

            ans = list()
            for i in range (1, A+1) :

                if i % 3 == 0 and i % 5 == 0:
                    ans.append("FizzBuzz")
                    continue
                elif i % 3 == 0:
                    ans.append("Fizz")
                elif i % 5 == 0:
                    ans.append("Buzz")
                else:
                    ans.append(i)
        
            return ans


obj = Solution()
print(obj.fizzBuzz(3))








