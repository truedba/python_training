#!/usr/local/bin/python3

# script has 3 functions for 3 different options mentioned in task - so 3 outputs will be printed


def equal_entrance(nums, flat_num):
    result = False
    if (int(nums[0])-1) % flat_num:
        print('NO that impossible for equal entrances')
    else:
        print('YES that may happen for equal entrances')
        result = True
    return result


def equal_floors(flat_num):
    d = 2
    while flat_num % d != 0:
        d += 1
    if d == flat_num:
        print('NO that impossible for equal floors')
    else:
        print('YES that may happen for equal floors')


def first_floor_diff(flat_num):
    d = 2
    while (flat_num+1) % d != 0:
        d += 1
    if d == (flat_num+1):
        print('NO in case 1st floor is 1 apt less')
    else:
        print('YES in case 1st floor is 1 apt less')


if __name__ == "__main__":
    nums = input('Enter comma separated flat numbers: ').split(',')
    flat_count = (int(nums[1]) - int(nums[0]) + 1)
    if equal_entrance(nums, flat_count):
        equal_floors(flat_count)
        first_floor_diff(flat_count)



