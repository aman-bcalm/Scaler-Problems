import pandas as pd

class Solution:

    #def solve(dt, rid, ph, ch, ma):
    def solve(self ,dt, rid, ph, ch, ma):
    # YOUR CODE GOES HERE
    # return a string where the required id's are space separated

        dict = {}
        dt = list(map(lambda x : pd.Timestamp(x), dt))
        #rid = list(map(lambda x : int(x), rid.split()))
        #ph = list(map(lambda x : int(x), ph.split()))
        #ch = list(map(lambda x : int(x), ch.split()))
        #ma = list(map(lambda x : int(x), ma.split()))

        
        for i in range(0, len(dt)):

            dt[i] =  dt[i] >= pd.Timestamp(2014,5,1)

            if dt[i] ==  True:
                av = (ph[i] + ch[i] + ma[i])/3
                dict[av] = rid[i]
        
        res = []
        for k in sorted(dict.keys()):
            res.append(str(dict[k]))

        
        res = ' '.join(res)
        return res

        
            


obj = Solution()
dt = '2015-12-06 2011-12-27 2015-09-07 2012-12-21 2020-02-13 2015-06-09 2013-03-21 2012-09-22 2013-06-19 2016-03-05 2017-08-27 2012-06-24 2018-11-20 2018-05-24 2019-08-17 2018-08-22 2021-02-07 2016-09-01 2015-03-11 2011-06-30 2019-11-15 2016-11-30 2019-05-19 2012-03-26 2020-08-11 2014-09-12 2014-12-11 2013-12-16 2017-02-28 2011-04-01 2011-01-01 2017-11-25 2014-03-16 2014-06-14 2013-09-17 2020-05-13 2018-02-23 2019-02-18 2011-09-28 2016-06-03 2020-11-09 2017-05-29'
rid = '498 721 375 464 813'
ph = '22 45 1 65 22'
ch = '52 56 32 50 24'
ma = '63 37 68 62 43'  
print(obj.solve(dt, rid, ph, ch, ma))

