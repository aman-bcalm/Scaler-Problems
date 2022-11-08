#Rotation game optimized
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    A = list(map(int, input().strip().split()))
    k = int(input())
    N = A.pop(0)
    if k > N :
        k = k % N

    #reverse the list
    A = A[::-1]    
    A = A[0:k:1][::-1] + A[k:len(A):1][::-1]
    print(A)
    return 0

if __name__ == '__main__':
    main()