def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    guess = int(len(aStr) / 2)
    if aStr == "":
        return False
    elif char == aStr[guess]:
        return True
    elif char > aStr[guess]:
        return isIn(char, aStr[guess + 1:])
    elif char < aStr[guess]:
        return isIn(char, aStr[:guess])
    else:
        return False


print(isIn('a', ''))