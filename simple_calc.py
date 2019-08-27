#!/usr/local/bin/python3

# this script is simple calc for 2 numbers

if __name__ == "__main__":

    operation = int(input('''
    Please choose operation id you need: 
    1. Add 
    2. Multiply 
    3. Extract 
    4. Divide 
    '''))

    if 0 < operation < 5:

        first_num = float(input('Please enter first number: '))
        last_num = float(input('Please enter second number: '))

        if operation == 1:
            result = first_num + last_num

        elif operation == 2:

            result = first_num * last_num

        elif operation == 3:

            result = first_num - last_num

        else:

            if last_num != 0:

                quotient = first_num // last_num
                remainder = first_num % last_num

            else:

                print('You are not allowed to divide on 0!')
                quit()

            print('quotient is ', int(quotient), ' remainder is ', remainder)
            quit()

        print(result)

    else:
        print('Operation id  is out of the range')


