


class Solution :


     def fun(self, s):
        # YOUR CODE GOES HERE
        # This function is for applying while filtering the input emails.


        #print(s)
        s = list(s)
        
        #check if there is @
        if '@' in s:

            apos = -1
            for i in range (0 ,len(s)):

                if '@' == s[i]:
                    apos = i
                    break
        else:
            #print("@ not found returning false")
            return False
        
        #0 to apos-1 has the 'username'
        for i in range(0, apos):

            if not(s[i].isalnum() or s[i] == '-' or s[i] == '_'):
                 #print("special character " + s[i] + " found returning false")
                 return False
        
        if '.' in s[apos+1: len(s)]:

            dpos = -1
            for i in range(apos+1, len(s)):

                if s[i] == '.':
                    dpos = i
                    break
        else:
            #print(". not found returning false")
            return False
        
        # apos+1 to dpos-1 is websitename

        for i in range(apos+1, dpos):

            if not(s[i].isalpha()):
                return False

        # dpos+1 to len(s) is the extenion
        # max length of extension is 3
        if len(s) - (dpos+1) > 3:
            return False

        return True        





     def filter_mail(self, emails):
        return list(filter( self.fun, emails))


obj = Solution()
emails = ['sara@scaler',
'brianfdsd-23@scaler.cm',
'fsdfbrute_54@scaler.co',
'sddfafa.fdd.cc',
'dwe.casd@fsd',
'fseefrwe.fsdfwed@fsedfs.ccas.com']

print(obj.filter_mail(emails))