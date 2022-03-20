def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    if a < 0:
        a *= -1
        return not a >= int(str(a)[::-1])
    return a >= int(str(a)[::-1])


print((main(-21)))
