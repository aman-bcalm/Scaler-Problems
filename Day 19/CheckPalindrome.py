import sys
sys.setrecursionlimit(10**6)

class Solution:


    # @param A : string
    # @return an integer
    def solve(self, A):     
        
        #print(A[0], A[len(A)-1])
        if len(A) == 1 or len(A) == 0:
            return 1
        #lenght is at least 2    
        elif A[0] != A[len(A)-1]:
            #print(A,A[0],A[len(A)-1])
            return 0
        else:
            #print(len(A))
            return self.solve(A[1:len(A)-1])

obj = Solution()
A = "mnschgziwincvcrhegtkkgzuewasvstiogqaijvtvikjjivatyqbnsrnfcrhxlkkrrqrmzemiqbujbktdnejobxtcjiibcfynrfxbbqwujyleetwwalbuewgewkdrefcdptqgpqhqvguniapbdzdxexeealxmtbmlsdihyllmnmltghyetghrtmpimqepumuzvkdmxvyoweexxckmyqtirjnebodjmuzozmvypdcalffowunzrlflvmimxhemvlhobeenpcvynchlxpsdvlmeddahnvkspuqhgrxdukrhtbtlpxyblucxuyoowsxgtqeiotylvonaublmozlvwsphfilxfncegpleebaiufdjmpiolgdbfcshbwjchuxumyxhhrujifbcehsniqpghdztvztxvliztiqzwaktqohpntxeyfeaijldzhnsyvhjixlymtmrfvzlqgdomawrfddcagjagvcfhbyqgixyqbbpyjijeviyhwrignduetolptfyvmklmdrxqvrdnwssvgujqfwukneddqdvvqxxmuhtxuiufbqxswstgrykpoeiizmbpoturgrnvsshhzoppyktljqxxuhcdfsmesaimxicxfslnfagdfaoczbhivhxmotzbpulduuczfyeijkkcwmqqtrqstwiqmkatyjotoexkeesprwzfxwzshwlqfssryxxvybnrxdiuusvnnlfabkpynsakpnftjqhecuwmyqgwhyrtudmkfcphnnyxqxzxbucfewihqmjjnblrmyertspotzfgzvabnhcxklqdlbtvvqwynenkkhxcjsndltankzkmrkknbkxjqzabatkcdvodhzzmqqcfwshhufezzddzrfldwxylaylpfqpiczfmyymfzcipqfplyalyxwdlfrzddzzefuhhswfcqqmzzhdovdcktabazqjxkbnkkrmkzknatldnsjcxhkknenywqvvtbldqlkxchnbavzgfztopstreymrlbnjjmqhiwefcubxzxqxynnhpcfkmdutryhwgqymwucehqjtfnpkasnypkbaflnnvsuuidxrnbyvxxyrssfqlwhszwxfzwrpseekxeotojytakmqiwtsqrtqqmwckkjieyfzcuudlupbztomxhvihbzcoafdgafnlsfxcixmiasemsfdchuxxqjltkyppozhhssvnrgrutopbmziieopkyrgtswsxqbfuiuxthumxxqvvdqddenkuwfqjugvsswndrvqxrdmlkmvyftploteudngirwhyivejijypbbqyxigqybhfcvgajgacddfrwamodgqlzvfrmtmylxijhvysnhzdljiaefyextnphoqtkawzqitzilvxtzvtzdhgpqinshecbfijurhhxymuxuhcjwbhscfbdgloipmjdfuiabeelpgecnfxlifhpswvlzomlbuanovlytoieqtgxswooyuxculbyxpltbthrkudxrghqupskvnhaddemlvdspxlhcnyvcpneebohlvmehxmimvlflrznuwofflacdpyvmzozumjdobenjritqymkcxxeewoyvxmdkvzumupeqmipmtrhgteyhgtlmnmllyhidslmbtmxlaeexexdzdbpainugvqhqpgqtpdcferdkwegweublawwteelyjuwqbbxfrnyfcbiijctxbojendtkbjubqimezmrqrrkklxhrcfnrsnbqytavijjkivtvjiaqgoitsvsaweuzgkktgehrcvcniwizghcsnm"
#print(len(A))
print(obj.solve(A))

