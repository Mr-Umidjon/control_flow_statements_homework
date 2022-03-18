def main(a, b, c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    return (a > 0) + (b > 0) + (c > 0)


print(main(1, 2, 0))
