

''''

   Helper functions

'''


def isNumber(x):
    '''
    Function that determines if x represents an integer.
    In: x - string
    Out: True - if x represents an integer
         False - otherwise
    '''

    try:
        float(x)
        return True
    except:
        return False


def isType(x):
    '''
    Function that determines if x is a valid expense type ("gas","heat","water","other","elec").
    In: x - string
    Out: True - if x is a valid expense type
         False - otherwise
    '''

    if x in ["gas","heat","water","other","elec"]:
        return True
    return False

''''

0. Getters and Setters

'''


def getApIndex(id,apartments):
    '''
    Finds and returns the index of an apartment with id <id>.
    In: id, apartments

    '''
    for index, i in enumerate(apartments):
        if id == getId(i):
            return index


def getApIdList(apartments):
    '''
    Function that returns a list of all apartments ids.
    In: apartments - apartments list
    Out: list of apartments ids
    '''

    lst = []
    for i in apartments:
        lst.append(getId(i))
    return lst



def getId(ap):
    '''
       Function that gets the id of an apartment.
       In: ap - apartment
       Out: the id of an apartment
       '''
    return ap["id"]


def getAmount(ap,type):
    '''
    Function that gets the amount of a given expense from an apartment.
    In: ap - apartment, type - the type of the expense
    Out: the amount of the requested expense
    '''

    return ap[type]


def setAmount(ap,type, val=0):
    '''
    Function that sets the amount of a given expense from an apartment.
    In: ap - apartment, type - the type of the expense, val - the new value / 0 by default
    Out: -
    Post: Sets the value of the expense to the value of <val>
    '''

    ap[type] = val




''''

1. Add a new transaction to the list

'''


def addExpense(ap,type,amount):
    '''
    Function that adds to an expense of a given apartment a given amount.
    In: ap - apartment
        type - string, type of the expense
        amount - float, value to be added
    '''
    newAmount = amount + getAmount(ap,type)
    setAmount(ap,type,newAmount)


def createExpense(id,water=0,heat=0,elec=0,gas=0,other=0):
    '''
    Function that creates a new apartment and then adds to an expense a given amount.
    In: ap - apartment
        type - string, type of the expense
        amount - float, value to be added
    '''

    return {"id": id, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0}


def createAddExpense(id,type,amount,apartments):
    '''
    Function that creates a new apartment and then adds to an expense a given amount.
    In: ap - apartment
        type - string, type of the expense
        amount - float, value to be added
    '''
    expense = createExpense(id,apartments)

    apartments.append(expense)
    addExpense(apartments[-1],type,amount)

''''

2. Modify expenses from the list.

'''


def removeApart(apartments,i,j):
    '''
     Function that clears expenses of apartments from i to j.
     In: apartments
         i,j - apartment ids
     Pre: i <= j
     Out: -
     Post: apartments from i to j have their expenses cleared
    '''

    for ap in apartments[i-1:j]:
       for type in ["gas","water","heat","elec","other"]:
            setAmount(ap,type)


def removeType(apartments,type):
    '''
    Function that clears the values of all <type> expenses.
    In: apartments
        type - type of expense
    Out: -
    Post: expenses of type have their values cleared
    '''

    for i in apartments:
        setAmount(i,type)


def replace(ap,type,amount):
    '''
    Function that replaces an expense of a given apartment.
    In: ap - apartment
        type - expense type
        amount - float value
    Out: -
    Post: the value of expense <type> of apartment <ap> is set to <amount>
    '''

    setAmount(ap,type,amount)


''''

3. Write the expenses having different properties.

'''


def toStr(ap):
    return str(getId(ap)) + " | water = " + str(getAmount(ap,"water")) + ", heat = " + str(getAmount(ap,"heat"))  + ", elec = " + str(getAmount(ap,"elec"))  + ", gas = " + str(getAmount(ap,"gas"))  + ", other = " + str(getAmount(ap,"other"))


def totalExpenses(ap):
    ''''
    Function that returns the sum of all expenses
    In: ap - apartment
    Out: - sum of all expenses
    '''
    s=0
    for type in ["water","heat","elec","gas","other"]:
        s+=getAmount(ap,type)

    return s


''''

4. Obtain different characteristics of the expenses.

'''


def sum(apartments, type):
    ''''
    Function that returns the sum of all expenses of a type.
    In: apartments - list of apartments
        type - valid type
    Out: sum of all expenses of type
    '''

    s=0
    for ap in apartments:
        s+= getAmount(ap,type)

    return s


def sortList(lst):
    l = len(lst)
    for i in range(0, l): 
        for j in range(0, l-i-1): 
            if (lst[j][1] > lst[j + 1][1]): 
                aux = lst[j]
                lst[j]= lst[j + 1] 
                lst[j + 1]= aux
    return lst


def sortApartment(apartments):
    ''''
    Function that returns a sorted list of total expenses of each apartment.
    In: apartments - apartments list
    Out: sorted apartemnts list
    '''
    lst = []

    for ap in apartments:
        lst.append([getId(ap), totalExpenses(ap)])

    return sortList(lst)


def sortType(apartments):
    ''''
     Function that returns a sorted list of total expenses of each type.
     In: apartments - apartments list
     Out: sorted types list
     '''
    lst = []

    for type in ["water", "heat", "elec", "gas", "other"]:
        lst.append([type, sum(apartments, type)])

    return sortList(lst)


def maxi(ap):

    lst = []
    maxim = -1

    for type in ap:
        if type in ["water", "heat", "elec", "gas", "other"]:
            if getAmount(ap,type) > maxim:
                maxim = getAmount(ap, type)

    for type in ["water", "heat", "elec", "gas", "other"]:
        if getAmount(ap,type) == maxim:
            lst.append([type, maxim])

    return lst


''''

5. Filter

'''

def filterType(apartments, type):

    for ap in apartments:
        for t in ap.keys():
            if t != "id" and t != type:
                setAmount(ap,t)


def filterAmount(apartments,val):

    for ap in apartments:
        for amount in ap.keys():
            if amount != "id":
                if ap[amount] < val:
                    setAmount(ap,amount)


'''

6. Undo the last operation that modified program data.

'''


def undo(apartments, undoList):
    '''
    Function that undos the last operation.
    In: apartments - apartments
        undoList - operation history
    Out: -
    '''
    apartments[:] = undoList[-1]
    undoList.pop()
