'''
Generate the first prime number larger than a given natural number n.v

'''


def isPrime(x):
    '''
    Function that determines if a given integer x is prime or not.
    Input:
        - x , integer
    Preconditions:
    Output:
        - bool value
    Postconditions:
        - true if the number x is prime
        - false if the number x is not prime
    '''

    if x == 2:
        return True

    if x % 2 == 0 or x < 2:
        return False

    d = 3
    while d*d <= x:
        if x % d == 0:
            return False
        d = d + 2
    return True

def primeNumLargerThanN(n):
    '''
    Funtion that returns the first prime number larger than a given integer n.
    Input:
        - n, integer
    Output:
        - x, integer, first prime number larger than n
    '''
    x = n + 1

    while not isPrime(x):
        x = x + 1

    return x

def printRes(n,x):

    print("The first prime number larger than ",n," is ",x,".")

# Test functions

def test_isPrime():

    assert isPrime(2)==True
    assert isPrime(1)==False
    assert isPrime(-10)==False
    assert isPrime(9)==True
    assert isPrime(25)==False

    return

def test_primeNumLargerThanN():

    assert primeNumLargerThanN(1)==2
    assert primeNumLargerThanN(5)==7

    return

def run_tests():

    test_isPrime()
    test_primeNumLargerThanN()

    return
###

def run():

    print(primeNumLargerThanN(int(input("Enter a number: "))))

    return


run()
