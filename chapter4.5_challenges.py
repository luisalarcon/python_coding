#Challenge 5
def toFloat(n):
    """
    Returns float value of a string.
    :param n: string.
    :returns: float of n.
    """
    try:
        return float(n)
    except(ValueError):
        print("invalid input")

print(toFloat("f"))

print(toFloat("3.14"))
