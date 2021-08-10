#library modul
import os
import sys

#Global variabel
result = 0.0
check = 1

#Pemeriksa input dan memproses input
def process(num1, num2, op):

    #Cek number 1
    try:
        val = float(num1)
    except ValueError:
        print("\nError: Number 1 is not number")
        if check == 1:
            main()
        else:
            lanjut()

    # Cek number 2
    try:
        val = float(num2)
    except ValueError:
        print("\nError: Number 2 is not number")
        if check == 1:
            main()
        else:
            lanjut()

    #typecasting
    num1 = float(num1)
    num2 = float(num2)

    #Proses aritmatika
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2

    #Cek operator
    else:
        print("\nError: Invalid operator")
        if check == 1:
            main()
        else:
            lanjut()

#Reset dan hitung lagi
def restart():
    x = input('\nCoba lagi?(y/n): ')
    if x.lower() == 'y':
        os.system("cls")
        main()

    elif x.lower() == 'n':
        print("\nTerima kasih ^^\n")
        sys.exit()

    else:
        print("\nError: please use 'n' or 'y'")
        restart()

#Mengoperasikan lagi
def lanjut():

    #Use global var
    global check
    global result

    check += 1
    x = input('lanjut?(y/n): ')
    if x.lower() == 'y':
        os.system("cls")
        print("\nResult(number 1): ",result)
        opAdd = input("Choose operator(+,-,*,/): ")
        numAdd = input("Enter number 2: ")
        result = process(result, numAdd, opAdd)
        print("\nResult: ", result)
        lanjut()

    elif x.lower() == 'n':
        restart()
    else:
        print("\nError: please use 'n' or 'y'\n")
        lanjut()

#Program Utama
def main():

    global result

    print("\n=== Simple Calculator ===")

    num1 = input("Enter number 1: ")
    op = input("Choose operator(+,-,*,/): ")
    num2 = input("Enter number 2: ")

    result = process(num1, num2, op)
    print("\nResult: ",result)

    #Loop program
    lanjut()

main()