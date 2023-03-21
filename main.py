
import math

Baseset = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F" ] ##base 16


def intro():
    print("WELCOME TO BASE-16! \n"
          "Please choose which calculation you wish to use \n"
          "ENTER: 1 - BASE-16 to decimal number \n"
          "ENTER: 2 - decimal number to BASE of n \n")
    try:
        choice = int(input())
        if choice == 1:
            base16()
        elif choice == 2:
            base_n()
        else:
            print("please choose a calculation")
            intro()

    except ValueError:
        print("Please choose a calculation")
        intro()


def base16():
    print("~BASE 16~")
    print("Please enter your Hexadecimal code/number: ")
    B = str(input())
    code = []
    decimal = 0
    for x in range(len(B)):
        code.append(B[x].upper())
    ##print(code)
    for x in range(len(code)):
        power = len(code) - 1 - x
        Basenum = 0
        for n in range(len(Baseset)):
            if code[x] == Baseset[n]:
                Basenum = n
        decimal = decimal + (Basenum * (16**power))
        ##print(str(code[x]) + str(power))
    print("decimal\BASE-16: " + str(B.upper()))
    print(" V ")
    print("decimal\BASE-10: " + str(decimal))

def base_n():
    print("BASE N")
    print("Please enter your Decimal number(base 10): ")
    B = int(input())
    print("Please enter what Base of N you want to convert(16-2): ")
    D = int(input())
    max_power = 0
    x = 0
    while x <= B:
        x = D**max_power
        ##print(x)
        max_power = max_power + 1
    max_power = max_power - 2
    code = []
    basenum = B
    while basenum > 0:
        code.append( Baseset[ math.floor( basenum/D**max_power)])
        basenum = basenum - ( (D**max_power) *  math.floor( basenum/D**max_power) )
        max_power = max_power - 1
    ##print(code)
    print("decimal\BASE-10: " + str(B))
    print(" V ")
    print("decimal\BASE of " + str(D) + ": " + (''.join(code)))



intro()
#base_n()