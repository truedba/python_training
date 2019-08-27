#!/usr/local/bin/python3

# this script will check whether u can buy N balls of ice cream


if __name__ == "__main__":

    ball_quantity = int(input('Enter desired number of balls: '))
    answer = 'NO'
    result = False

    for i in range((ball_quantity // 5)+1):
        if (ball_quantity - i * 5) % 3 == 0:
            result = True

    if ball_quantity % 3 == 0 or  ball_quantity % 5 == 0 or result:
        answer = 'Yes'

    print(answer)

