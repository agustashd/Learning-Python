def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    def evaluate(x):
      poly = 0
      for n in L:
        poly += n * (x ** (len(L) - L.index(n) - 1))

      return poly

    return evaluate

print(general_poly([0, -2, 3, 4])(10))

'''
OTRA OPCION
    def to_apply (x):
        n = 0
        for i in L:
            n = x*n + i
        return n
'''