def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    t = int(input())
    while(t>0):
        
        lst =  list(map(int, input().strip().split()))
        even = 0
        odd = 0
        for i in range (1,len(lst)) :
            if lst[i] % 2 == 0:
                even += 1
            else :
                odd += 1
        print(abs(even-odd))
        t -=1
        
        


if __name__ == '__main__':
    main()