'''
The numbers n1 and n2 have the property P if their writings in basis 10 have the same digits
(e.g. 2113 and 323121). Determine whether two given natural numbers have the property P.
'''
def verifyPropertyP(n1,n2):
    '''
    Function that determines if 2 given integers have the same digits.
    Input:
        n1, n2
    Preconditions:
        n1 - integer, n2 - integer
    Output:
        bool
    Postconditions:
        True - if the numbers have the same digits
        False - otherwise
        '''
    n1Digits = set(str(n1))
    n2Digits = set(str(n2))

    if len( n1Digits.difference(n2Digits) ) == 0:
        return True
    else:
        return False

def run_tests():

    assert verifyPropertyP(123,312) == True
    assert verifyPropertyP(111,222) == False
    assert verifyPropertyP(762,9872) == False
    assert verifyPropertyP(123,12333) == True


def run():

    n1 = int( input("Enter the first number: ") )
    n2 = int( input("Enter the second number: ") )

    if verifyPropertyP(n1,n2):
        print("The given numbers have the property P.")
    else:
        print("The given numbers don't have the property P.")

    return


run_tests()
run()
