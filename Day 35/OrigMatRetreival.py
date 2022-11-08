import numpy as np
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()' for input & 'print' for output
    T = 4
    res = np.zeros(4).reshape(2,2)
    res1 = np.zeros(4).reshape(2,2)
    while T > 0:

        a = list(map(lambda x:int(x), input().split()))
        s = a[0]
        e = a[1]
        mt = np.arange(s, e+1, round((e-s) / 3a ), dtype = 'float64').reshape(2,2)
       
        if T == 4:
            res = mt
        elif T == 3:
            res = np.append(res, mt, axis = 1)
        elif T == 2:
            res1 = mt
        elif T == 1:
            res1 = np.append(res1, mt, axis = 1)


        T -= 1

    res = np.append(res, res1, axis = 0)
    print(res)

    return 0

if __name__ == '__main__':
    main()