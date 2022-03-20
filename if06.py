def main(a, b, c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    count = a > 0 + b > 0 + c > 0
    count2 = a < 0 + b < 0 + c < 0
    if count > count2:
        result = "there are a lot of positive numbers"
    else:
        result = "there are a lot of negative numbers"
    return result
