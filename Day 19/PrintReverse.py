import sys
sys.setrecursionlimit(10**6)

def reverse( A):
    if len(A) == 1:
        return A
    else:
        return A[len(A)-1] + reverse(A[0:len(A)-1])


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    str = input()
    print(reverse(str))
    return 0

if __name__ == '__main__':
    main()