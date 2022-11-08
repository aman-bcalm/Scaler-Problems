def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    t = int(input())
    while t > 0:
       a = input().split()[1:]
       a = [int(x) for x in a]
       a.sort(reverse = True)
       if len(a) >= 2:
             print(a[1])
       else:
             print(-1)
       t -= 1

    return 0

if __name__ == '__main__':
    main()