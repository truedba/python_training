#!/usr/local/bin/python3

# this script swap 2 numbers

if __name__ == "__main__":

    first_var = int(input('Please enter first variable: '))
    second_var = int(input('Please enter second  variable: '))
    first_var = first_var ^ second_var
    second_var = first_var ^ second_var
    first_var = first_var ^ second_var
    print('first variable is: ', first_var,'\nsecond variable is: ',second_var)
