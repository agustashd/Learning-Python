def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    n = 0
    result = 0
    while result <= x:
      n += 1
      result = b ** n
    return n - 1

print(myLog(16,2))