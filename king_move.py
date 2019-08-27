#!/usr/local/bin/python3

# this script will check whether king can make move specified by user


if __name__ == "__main__":

    init_pos = input('Enter initial king position: ')
    final_pos = input('Enter final king position: ')

    x1 = int(init_pos.split(',')[0])
    y1 = int(init_pos.split(',')[1])
    x2 = int(final_pos.split(',')[0])
    y2 = int(final_pos.split(',')[1])

    if (x2-x1 == 0 and y2-y1 == 0) or x1 > 7 or x2 > 7 or y1 > 7 or y2 > 7:
        print('Coordinates are equal or impossible')
    else:
        if (x2-x1) ** 2 < 2 and (y2-y1) ** 2 < 2:
            print('YES')
        else:
            print('NO')
