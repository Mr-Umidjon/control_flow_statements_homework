def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if 9 < a < 100 and a % 2 == 1:
        reslut = "two-digit odd number"
    if 9 < a < 100 and a % 2 == 0:
        reslut = "two-digit even number"

    if 99 < a < 1000 and a % 2 == 1:
        reslut = "two-digit odd number"
    if 99 < a < 1000 and a % 2 == 0:
        reslut = "two-digit even number"

    return reslut
