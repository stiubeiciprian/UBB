from math import sqrt

'''
String to float
'''
def strToFloat(x):
    '''
    Function that takes the imaginary part and the real part out of a string and converts them to float type.
    Input: x - string formated like a+bi , where a,b are  real numbers
    Output: [ a' , b' ] a' = float(a), b' = float(b)
    '''
    i = 1
    while i < len(x):
        if x[i] == "-" or x[i] == "+":
            break
        i += 1

    real = x[:i]
    imag = x[i:]

    real = float(real)
    imag = float(imag)

    return [real,imag]

'''
Longest Sequence
'''
def longestSameDigitsSequence(numList):

    '''
    Function that returns the start and end indices of the longest subsequence of numbers with the real and imaginary part composed of the same digits.
    Input: numList - list of complex numbers
    Output: dictionary { "st": stMax, "dr": drMax } where stMax is the start index of the subsequence and drMax the end index + 1
    '''

    l=0
    lMax=0
    st=0
    stMax = 0
    drMax=0

    for i in range(0,len(numList)):

        real = getReal(numList[i])
        imag = getImag(numList[i])

        if sameDigits(real,imag):
            if l == 0:
                st = i
            l+=1
        else:
            if l >= lMax and l!=0:
                lMax = l
                drMax = i
                stMax= st
            l = 0

    if l >= lMax and l!=0:
        lMax = l
        stMax = st
        drMax = i+1

    return { "st": stMax, "dr": drMax }


def longestRealNumSequence(numList):

    '''
    Function that returns the start and end indices of the longest subsequence of real numbers present in numList.
    Input: numList - list of complex numbers stored as dictionaries, { "real": <value>, "imag": <value> }
    Output: dictionary { "st": stMax, "dr": drMax } where stMax is the start index of the subsequence and drMax the end index + 1
    '''

    l=0
    lMax=0
    st=0
    stMax=0
    drMax=0

    for i in range(0,len(numList)):
        if getImag(numList[i]) == 0:
            if l == 0:
                st = i
            l+=1
        else:
            if l >= lMax and l!=0:
                lMax = l
                drMax = i
                stMax= st
            l = 0

    if l >= lMax and l!=0:
        lMax = l
        stMax = st
        drMax = i+1

    return { "st": stMax, "dr": drMax }

def longestEqualModSequence(numList):

    '''
    Function that returns the start and end indices of the longest subsequence of numbers with modulus in [0,10] from numList.
    Input: numList - list of complex numbers
    Output: dictionary { "st": stMax, "dr": drMax } where stMax is the start index of the subsequence and drMax the end index + 1
    '''

    l=0
    lMax=0
    st=0
    stMax = 0
    drMax=0

    for i in range(0,len(numList)):

        real = getReal(numList[i])
        imag = getImag(numList[i])

        if sqrt(real*real + imag*imag) <= 10:
            if l == 0:
                st = i
            l+=1
        else:
            if l >= lMax and l!=0:
                lMax = l
                drMax = i
                stMax= st
            l = 0

    if l >= lMax and l!=0:
        lMax = l
        stMax = st
        drMax = i+1

    return { "st": stMax, "dr": drMax }
'''
2 numbers same digits
'''

def sameDigits(n1,n2):
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
    n1Digits = set(str(n1).replace('.',''))
    n2Digits = set(str(n2).replace('.',''))

    if len( n1Digits.difference(n2Digits) ) == 0:
        return True
    else:
        return False

'''
Print functions
'''

def print_longestSequence(numList,pos):
    '''
    Function that prints a subsequence of complex numbers
    Input: numList - list of complex numbers stored as dictionaries, { "real": <value>, "imag": <value> }
    Output: dictionary { "st": stMax, "dr": drMax } where stMax is the start index of the subsequence and drMax the end index + 1
    '''
    try:
        printList(numList[pos["st"]:pos["dr"]])
    except:
        print("No subsequence found.")

    return

def printMenu():
    print()
    print('Command list:')
    print(' list - prints complex number list')
    print(' add -  adds complex number to list')
    print(' real - print longest sequence composed of real numbers')
    print(' mod - print longest sequence composed of numbers with modulus <=10')
    print(' exit - exits program')
    print()
    return

def printList(lst):
    '''
    Function that prints list of complex numbers.
    Input: lst - list of complex numbers stored as dictionaries, { "real": <value>, "imag": <value> }
    Output: -
    '''
    for x in lst:
        print(toStr(x))
    return

'''
Setters and getters
'''

def createComplex(a,b):
    '''
    Function that creates a complex number c given its real part a and imag part b
    Input: a,b
    Prec: a,b - float
    Output: c
    Postc: c -complex number
        The real part of c = a
        The imaginary part of c = b
    '''
    return {"real":a, "imag":b}

def getReal(c):
    '''
    Function that gets the real part of the given complex number c
    Input: c
    Prec: c - complex
    Output: r
    Post: r is the real part of c, r -float
    '''
    return c["real"]

def getImag(c):
    '''
    Function that gets the imaginary part of the given complex number c
    Input: c
    Prec: c - complex
    Output: r
    Post: r is the real part of c, r -float
    '''
    return c["imag"]

def setReal(c,x):
    '''
    Function that sets the real part of the given  complex number c
    nput: c
    Prec: c - complex
    Output: cc
    Post: cc
            the real part of cc is x
            the imag part of cc is the imag part of c
    '''
    return { "real":x, "imag":c["imag"] }

def setImag(c,x):
    '''
    Function that sets the imaginary part of the given  complex number c
    nput: c
    Prec: c - complex
    Output: cc
    Post: cc
            the real part of cc is the real part of c
            the imag part of cc is x
    '''
    return { "real":c["real"], "imag":x }

def toStr(c):
    if getImag(c)>=0:
        return str(c["real"])+"+"+str(c["imag"])+"i"
    else:
        return str(c["real"]) + str(c["imag"]) + "i"

'''
ui functions
'''


def ui_read():
    '''
    Function that takes the real part and the imaginary part of a number z from a string formated like: a+bi.
    Input: string formated like a+bi where a,b are real numbers.
    Output: [ real, imag ] where real = float(a) and imag = float(b)
    '''

    x = input("Enter complex number:")
    x = x.replace(' ', '')
    x = x.replace('i', '')

    return strToFloat(x)


def ui_addToList(lst):
    '''
    Function that appends complex z number to a list of complex numbers.
    Input: lst - list of dictionaries
            lst = [ c1, c2, ... , cn ]
    Output: lst' = [ c1, c2, ..., cn , z ]
    '''
    try:
        res = ui_read()
        c = createComplex(res[0],res[1])
        lst.append(c)
    except:
        print("Invalid input!")
        ui_addToList(lst)

    return

def ui_longestEqualModSequence(numList):

    pos = longestEqualModSequence(numList)

    print_longestSequence(numList,pos)

    return

def ui_longestRealNumSequence(numList):

    pos = longestRealNumSequence(numList)

    print_longestSequence(numList,pos)

    return

def ui_longestSameDigitsSequence(numList):

    pos = longestSameDigitsSequence(numList)

    print_longestSequence(numList,pos)

    return

'''
Tests
'''
def test_strToFloat():

    str = "1.12+2.45"
    assert strToFloat(str) == [1.12,2.45]

    str = "1.0-4.32"
    assert strToFloat(str) == [1.0, -4.32]

    str = "-2-1.23"
    assert strToFloat(str) == [-2,-1.23]

    return
def test_CreateComplex():
    real = 1.23
    imag = -2.23
    c = createComplex(real,imag)
    assert getReal(c)==real
    assert getImag(c)==imag

    d=-9
    c = setReal(c,d)
    assert getReal(c)==d
    assert getImag(c)==imag
    return

def test_longestRealNumSequence():
    testList = [
                {"real":0, "imag":2},
                {"real":1, "imag":0},
                {"real":3, "imag":0}
    ]
    assert longestRealNumSequence(testList) == { "st": 1, "dr": 3 }
    testList = [
                {"real":0, "imag":1},
                {"real":1, "imag":2},
                {"real":3, "imag":0},
                {"real":3, "imag":0},
                {"real":3, "imag":0},
                {"real":3, "imag":3}
    ]
    assert longestRealNumSequence(testList) == { "st": 2, "dr": 5 }
    testList = [
                {"real":0, "imag":2},
                {"real":1, "imag":2},
                {"real":3, "imag":2},
    ]
    assert longestRealNumSequence(testList) == { "st": 0, "dr": 0 }
    return

def test_longestEqualModSequence():
    testList = [
                {"real":10, "imag":21},
                {"real":1, "imag":0},
                {"real":3, "imag":0}
    ]
    assert longestEqualModSequence(testList) == { "st": 1, "dr": 3 }
    testList = [
                {"real":12, "imag":12},
                {"real":11, "imag":11},
                {"real":3, "imag":0},
                {"real":3, "imag":0},
                {"real":3, "imag":0},
                {"real":3, "imag":32}
    ]
    assert longestEqualModSequence(testList) == { "st": 2, "dr": 5 }
    testList = [
                {"real":0, "imag":20},
                {"real":1, "imag":20},
                {"real":3, "imag":20},
    ]
    assert longestEqualModSequence(testList) == { "st": 0, "dr": 0 }
    return

def test_sameDigits():

    assert sameDigits(123,312) == True
    assert sameDigits(111,222) == False
    assert sameDigits(762,9872) == False
    assert sameDigits(123,12333) == True
    return

def runTests():

    test_sameDigits()
    test_strToFloat()
    test_CreateComplex()
    test_longestEqualModSequence()
    test_longestRealNumSequence()

'''
Program
'''
def start():
    numList = [
        {"real":0, "imag":2},
        {"real":1, "imag":0},
        {"real":3, "imag":0},
        {"real":4, "imag":0},
        {"real":3, "imag":3},
        {"real":1, "imag":1},
        {"real":3, "imag":2},
        {"real":7, "imag":10},
        {"real":2, "imag":0},
        {"real":9, "imag":0}
    ]
    commands = { 'add': ui_addToList, 'list': printList, 'real':ui_longestRealNumSequence, 'mod':ui_longestEqualModSequence, 'read':ui_read, 'digits':ui_longestSameDigitsSequence}

    while True:
        printMenu()
        cmd = input(">>")
        if cmd in commands.keys():
            commands[cmd](numList)
        elif cmd == 'exit':
            return
        else: print('Invalid command!')



runTests()
start()
