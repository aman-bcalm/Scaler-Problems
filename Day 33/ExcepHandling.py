def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output

    T =  int(input())
    while T > 0:
        i = input()
       
        try:
            ie = list(map(lambda x: int(x), i.split()))
            a = ie[0]
            b = ie[1]
            r = int(a/b)
            print(r)
        except ZeroDivisionError as e:
             print("Error Code: integer division or modulo by zero")
        except ValueError as e:
            print("Error Code:", e)
        
        T -= 1





    return 0

if __name__ == '__main__':
    main()   