def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    tc = int(input())
    while tc > 0:
        a = input()
        b = input()
        a = a.split()[1:]
        b = b.split()[1:]
        a = [int(x) for x in a]
        b = [int(x) for x in b]
        c = a + b
        c.sort()
        #for i in range(len(c)):
        for i in range(0, len(c)):
            print(c[i], end = ' ')
        print()
        tc -= 1
    #print(a, type(a))
    #print(b, type(b))
    return 0

if __name__ == '__main__':
    main()