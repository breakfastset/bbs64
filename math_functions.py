def get_determinant(a, b, c):
    """Calculate determinant of a quadratic equation."""
    return b ** 2 - 4 * a * c

def cube(number):
    """Return the cube of number."""
    return number * number * number

def integer_division(number, divisor):
    """Get the quotient and remainder from division."""
    quotient = number // divisor
    remainder = number % divisor
    return quotient, remainder