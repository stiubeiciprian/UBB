from tests import *
from copy import deepcopy


def ui_help():
    print(" add <apartament> <type> <amount>")
    print(" remove <apartment> / remove <start apartment> to <end apartment> / remove <type>")
    print(" replace <apartment> <type> with <amount>")
    print(" list / list <apartment> / list [<,=,>] <amount>")
    print(" sum <type>")
    print(" max <apartment>")
    print(" sort apartment")
    print(" sort type")
    print(" filter <type>")
    print(" filter <value>")
    print(" help")
    print(" exit")


''''

1. Add a new transaction to the list

'''


def ui_addExpense(apartments, undoList, x):

    if len(x) < 4:
        print("Not enough parameters!")

    elif len(x) > 4:
        print("Too many parameters!")
    else:
        copy = deepcopy(apartments)
        try:
            id = int(x[1])
            type = x[2]
            amount = float(x[3])

            if amount < 0:
                print("Cannot add negative value!")
                return

            if id in getApIdList(apartments):

                index = getApIndex(id, apartments)
                addExpense(apartments[index], type, amount)
            else:
                createAddExpense(id, type, amount, apartments)
        except:
            print("Invalid parameter!")
            return

        undoList.append(copy)


''''

2. Modify expenses from the list.

'''


def ui_remove(apartments, undoList, command):
    copy = deepcopy(apartments)
    if len(command) == 4:
        if command[2] == "to":
            try:
                i = int(command[1])
                j = int(command[3])
            except:
                print("Invalid parameter!")
                return
            removeApart(apartments, i, j)
        else:
            print("Invalid command!")
            return
    elif len(command) == 2:
        if isNumber(command[1]):
                i = int(command[1])
                removeApart(apartments, i, i)
        elif isType(command[1]):
            removeType(apartments, command[1])
        else:
            print("Invalid parameter!")
            return
    else:
        print("Invalid command!")
        return
    undoList.append(copy)


def ui_replace(apartments, undoList, x):

    if len(x) != 5:
        print("Invalid command!")
        return
    elif isNumber(x[1]) and isType(x[2]) and x[3] == "with" and isNumber(x[4]):
        copy = deepcopy(apartments)
        id = int(x[1])
        type = x[2]
        amount = float(x[4])

        if amount < 0:
            print("Cannot replace with negative value!")
            return

        if id in getApIdList(apartments):

            index = getApIndex(id, apartments)
            replace(apartments[index], type, amount)

        else:
            print("Apartment does not exit!")
            return
    else:
        print("Invalid command!")
        return

    undoList.append(copy)


''''

3. Write the expenses having different properties.

'''


def ui_print(apartments, cmd):
    length = len(cmd)
    if length == 1:
        print_apartments(apartments)
    elif length == 2:
        if isNumber(cmd[1]):
            index = getApIndex(int(cmd[1]), apartments)
            print_apartment(apartments[index])
        else:
            print("Invalid parameter!")
            return
    elif length == 3 and cmd[1] in ['<', '>', '='] and isNumber(cmd[2]):
        print_compare(apartments, cmd)
    else:
        print("Invalid command!")
        return


def print_apartments(apartments):
    '''
    Function that prints the apartments list.
    In: apartments
    Out: -
    '''
    for i in apartments:
        print(toStr(i))


def print_apartment(ap):
    '''
    Function that prints an apartment.
    In: apartment
    Out: -
    '''
    print(toStr(ap))


def print_compare(apartments, x):
    '''
    Function that prints
    '''
    if x[1] == '=':
        for i in apartments:
            if totalExpenses(i) == float(x[2]):
                print_apartment(i)
    elif x[1] == '<':
        for i in apartments:
            if totalExpenses(i) < float(x[2]):
                print_apartment(i)
    else:
        for i in apartments:
            if totalExpenses(i) > float(x[2]):
                print_apartment(i)


''''

4. Obtain different characteristics of the expenses.

'''


def ui_sum(apartments, cmd):

    if len(cmd) == 2 and isType(cmd[1]):
        print("The total amount for the expenses having type '" + cmd[1] + "' : " + str(sum(apartments, cmd[1])))
    else:
        print("Invalid command!")
        return


def print_sort(lst):

    for i in lst:
        print(str(i[0]) + " | Total expenses: " + str(i[1]) )


def ui_sort(apartments, cmd):

    if len(cmd) != 2:
        print("Invalid command!")
        return
    elif cmd[1] == "apartments":
        lst = sortApartment(apartments)
        print_sort(lst)
    elif cmd[1] == "type":
        lst = sortType(apartments)
        print_sort(lst)
    else:
        print("Invalid parameter!")
        return


def print_maxi(lst):
    for i in lst:
        print(i[0] + " : " + str(i[1]))


def ui_max(apartments, cmd):

    if len(cmd) != 2:
        print("Invalid command!")
        return
    elif isNumber(cmd[1]):
        print("Maximum expenses for apartment " + cmd[1] + ":")
        maximList = maxi(apartments[ getApIndex(int(cmd[1]), apartments) ])
        print_maxi(maximList)
    else:
        print("Invalid parameter!")
        return


''''

5. Filter

'''


def ui_filter(apartaments, undoList, cmd):

    copy = deepcopy(apartaments)
    if len(cmd) != 2:
        print("Invalid command!")
        return
    elif isNumber(cmd[1]):
        filterAmount(apartaments, float(cmd[1]))
    elif isType(cmd[1]):
        filterType(apartaments, cmd[1])
    else:
        print("Invalid command!")
        return

    undoList.append(copy)


''''

6. Undo the last operation that modified program data.

'''


def ui_undo(apartments, undoList):

    if len(undoList) <= 0:
        print("Cannot undo!")
    else:
        undo(apartments, undoList)
