#!/usr/local/bin/python3

# this script is made to deliver id of bigger number or 0 if equal

if __name__ == "__main__":

    num1 = int(input('Please enter first number: '))
    num2 = int(input('Please enter second number: '))
    if num1 - num2 > 0:
        print('1')
    elif num1 - num2 < 0:
        print('2')
    else:
        print('0')

