def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    global reslut
    if temp <= 0:
        reslut = "Freezing"
    if 1 <= temp <= 10:
        reslut = "Very Cold"
    if 11 <= temp <= 20:
        reslut = "Cold"
    if 21 <= temp <= 30:
        reslut = "Normal"
    if 31 <= temp <= 40:
        reslut = "Hot"
    if 41 <= temp:
        reslut = "Very Hot"

    return reslut
