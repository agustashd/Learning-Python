from math import *
def polysum(n, s):
    '''
    n, s: positive integers, n = number of sides and s = length
    returns: the sum of the are and the square perimeter rounded
    to four decimal places
    '''
    area = (0.25 * n * (s**2)) / tan(pi / n)
    perimeter = s * n
    return round(area + perimeter**2, 4)

print(polysum(5, 7))