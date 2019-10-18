
'''
Consider a given natural number n. Determine the product p of all the proper factors of n.
'''
def productOfProperFactors(n):

    '''
    Function that computes the product of the proper factors of a given natural number n.
    Input: n, natural number
    Output:
        0 if n<=3
        result, the product of proper factors of n, if n>3

    '''

    if n<=3: return 0

    result = 1
    fact = 2

    while fact * fact < n:
        if n % fact == 0:
            result = result * fact * n / fact
        fact = fact + 1

    if fact*fact == n:
        result = result * fact

    return result

def run_tests():

    assert productOfProperFactors(5) == 1
    assert productOfProperFactors(10) == 10
    assert productOfProperFactors(2) == 0

    return


def run():

    print(productOfProperFactors(int(input("Enter a natural number: "))))

    return

run_tests()
run()
