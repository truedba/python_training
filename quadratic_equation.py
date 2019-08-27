#!/usr/local/bin/python3

# this script will solve quadratic equation with factors specified by user

if __name__ == "__main__":

    a = float(input("Enter factor a: "))
    b = float(input("Enter factor b: "))
    c = float(input("Enter factor c: "))
    discriminant = (b ** 2) - (4 * a * c)

    if abs(a) < 0.0000001:

        print('This equation is linear, skipping')
        quit()

    if discriminant > 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        print(x1, x2)
    elif discriminant < 0.0000001 and a + b > 0:
        x = -b / (2 * a)
        print('solutions are equal and = ', x)
    else:
        print("No solutions")
