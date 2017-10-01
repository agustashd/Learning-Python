def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    #YOUR CODE HERE
    if b == 0:
      return a
    else:
      return gcd(b, a % b)

print(gcd(36,72))
