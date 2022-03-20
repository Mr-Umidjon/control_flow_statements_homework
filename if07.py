def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    global result
    if a > 0 and a % 2 == 1:
        result = "positive odd number"
    if a > 0 and a % 2 == 0:
        result = "positive even number"

    if a < 0 and a % 2 == 1:
        result = "negative odd number"
    if a < 0 and a % 2 == 0:
        result = "negative even number"

    if a == 0:
        result = "the number is zero"

    return result
