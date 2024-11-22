from math_functions import *


def main():
    num = 11
    result = cube(num)  # cube(11) will evaluate to 1331
    # result = 1331,   assign the 1331 to result to store the value returned
    print(f"Cube of {num} = {result}")

    # 2x^2 + 8x + 15 = 0
    determinant = get_determinant(2, 8, 15)
    print(f"Determinant: {determinant}")

    cube(10)  # 1000, this is lost because no variable to store it

    my_quotient, my_remainder = integer_division(19, 5)
    print(f"{my_quotient} remainder {my_remainder}")

main()   # call the main() to start program