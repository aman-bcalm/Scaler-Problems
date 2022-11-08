def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    t = int(input())
    while t > 0:

        a1 = list(map(int,input().strip().split()))
        a2 = list(map(int,input().strip().split()))
        l1 = a1[0]
        l2 = a2[0]
        a1.pop(0)
        a2.pop(0)

        res = []
        i= 0
        j= 0
        while(1):

            if(i > l1-1):
                res = res + a2[j:l2:1]
                break
            elif(j > l2-1):
                res = res + a1[i:l1:1]
                break
            else:
                if a1[i] < a2[j]:
                    res.append(a1[i])
                    i += 1
                else:
                    res.append(a2[j])
                    j += 1

        res = " ".join(map(str,res)) + " "
        print(res)


        
        t -= 1


    


if __name__ == '__main__':
    main()