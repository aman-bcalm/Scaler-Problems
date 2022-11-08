def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    c = input()
    vwl = ['a', 'e', 'i', 'o', 'u']
    if c in vwl:
        print(1)
    else:
        print(0)
    return 0

if __name__ == '__main__':
    main()