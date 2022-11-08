def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    units = input()
    units = int(units)

    bill = 0
    if units <= 50:
        bill = 0.50 * units
    elif units > 50 and units <= 150:
        bill = (0.50 * 50) + (units - 50) * 0.75
    elif units > 150 and units <= 250:
        bill = (0.50 * 50) + (100 * 0.75) + ((units - 150) * 1.20) 
    elif units > 250:
        bill = (0.50 * 50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)
    
    srch = 0.2 * bill
    bill =  bill + srch
    #shud be round but solution needs int whihc is round down
    bill = int(bill)
    return 0

if __name__ == '__main__':
    main()