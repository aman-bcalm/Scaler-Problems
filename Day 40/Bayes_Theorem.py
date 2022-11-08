class Solution:

    def solve(self, prior,positive_covid,positive_not_covid):
        # YOUR CODE GOES HERE
        
        prior = float(prior)
        not_prior = 1 - prior
        positive_covid = float(positive_covid)
        positive_not_covid = float(positive_not_covid)

        positive = (positive_covid * prior) + (positive_not_covid * not_prior) 
        positive_and_prior = positive_covid * prior
        ans = positive_and_prior / positive
        ans = round(ans, 3)
        return ans


obj = Solution()
print(obj.solve(0.6, 0.9, 0.1))
