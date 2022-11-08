def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = list(map(int, input().strip().split()))
    B = int(input())
    size = A.pop(0)
    last_i = len(A) - 1

    while B > 0 :
        last = A[last_i]
        for i in range (size-1,0,-1):
            A[i] = A[i-1]
        A[0] = last
        
        

        B = B-1

    ans = " ".join(map(str, A))
    print(ans)


    return 0

if __name__ == '__main__':
    main()