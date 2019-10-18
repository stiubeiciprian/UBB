from functionalities import *
from copy import deepcopy

def test_createExpense():
    list = [
        {"id": 1, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0},
        {"id": 2, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0},
        {"id": 3, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0}
    ]

    createAddExpense(4,"water",10,list)

    assert list == [
        {"id": 1, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0},
        {"id": 2, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0},
        {"id": 3, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0},
        {"id": 4, "water": 10, "heat": 0, "elec": 0, "gas": 0, "other": 0}
    ]


    createAddExpense(12,"heat",10,list)

    assert list == [
        {"id": 1, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0},
        {"id": 2, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0},
        {"id": 3, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0},
        {"id": 4, "water": 10, "heat": 0, "elec": 0, "gas": 0, "other": 0},
        {"id": 12, "water": 0, "heat": 10, "elec": 0, "gas": 0, "other": 0}
    ]


def test_getApIdList():
    list = [
        {"id": 1, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0},
        {"id": 2, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0},
        {"id": 3, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0}
    ]
    assert getApIdList(list) == [1,2,3]


def test_getAmount():

    ap = { "id":1, "water": 0, "heat": 0, "elec": 0, "gas": 12, "other": 24}

    assert getAmount(ap,"gas") == 12
    assert getAmount(ap, "other") == 24
    assert getAmount(ap, "water") == 0

def test_getId():

    ap = { "id":1, "water": 0, "heat": 0, "elec": 0, "gas": 12, "other": 24}

    assert getId(ap) == 1

    ap = {"id": 5, "water": 0, "heat": 0, "elec": 0, "gas": 12, "other": 24}

    assert getId(ap) == 5

def test_setAmount():
    ap = {"id": 1, "water": 0, "heat": 0, "elec": 0, "gas": 12, "other": 24}

    setAmount(ap,"heat",22)
    assert ap == {"id": 1, "water": 0, "heat": 22, "elec": 0, "gas": 12, "other": 24}

    setAmount(ap,"gas")
    assert  ap == {"id": 1, "water": 0, "heat": 22, "elec": 0, "gas": 0, "other": 24}


def test_removeApart():
    list = [
        {"id": 1, "water": 1, "heat": 1, "elec": 1, "gas": 1, "other": 0},
        {"id": 2, "water": 2, "heat": 0, "elec": 2, "gas": 0, "other": 0},
        {"id": 3, "water": 0, "heat": 3, "elec": 0, "gas": 3, "other": 0},
        {"id": 4, "water": 4, "heat": 4, "elec": 4, "gas": 4, "other": 4},
        {"id": 5, "water": 5, "heat": 0, "elec": 5, "gas": 0, "other": 0},
        {"id": 6, "water": 0, "heat": 6, "elec": 0, "gas": 0, "other": 6}
    ]

    removeApart(list,1,3)
    assert list == [
        {'id': 1, 'water': 0, 'heat': 0, 'elec': 0, 'gas': 0, 'other': 0},
        {'id': 2, 'water': 0, 'heat': 0, 'elec': 0, 'gas': 0, 'other': 0},
        {'id': 3, 'water': 0, 'heat': 0, 'elec': 0, 'gas': 0, 'other': 0},
        {'id': 4, 'water': 4, 'heat': 4, 'elec': 4, 'gas': 4, 'other': 4},
        {'id': 5, 'water': 5, 'heat': 0, 'elec': 5, 'gas': 0, 'other': 0},
        {'id': 6, 'water': 0, 'heat': 6, 'elec': 0, 'gas': 0, 'other': 6}
    ]

    removeApart(list,6,6)
    assert list == [
        {'id': 1, 'water': 0, 'heat': 0, 'elec': 0, 'gas': 0, 'other': 0},
        {'id': 2, 'water': 0, 'heat': 0, 'elec': 0, 'gas': 0, 'other': 0},
        {'id': 3, 'water': 0, 'heat': 0, 'elec': 0, 'gas': 0, 'other': 0},
        {'id': 4, 'water': 4, 'heat': 4, 'elec': 4, 'gas': 4, 'other': 4},
        {'id': 5, 'water': 5, 'heat': 0, 'elec': 5, 'gas': 0, 'other': 0},
        {'id': 6, 'water': 0, 'heat': 0, 'elec': 0, 'gas': 0, 'other': 0}
    ]


def test_removeType():
    list = [
        {"id": 1, "water": 1, "heat": 1, "elec": 1, "gas": 1, "other": 0},
        {"id": 2, "water": 2, "heat": 0, "elec": 2, "gas": 0, "other": 0},
        {"id": 3, "water": 0, "heat": 3, "elec": 0, "gas": 3, "other": 0},
        {"id": 4, "water": 4, "heat": 4, "elec": 4, "gas": 4, "other": 4},
        {"id": 5, "water": 5, "heat": 0, "elec": 5, "gas": 0, "other": 0},
        {"id": 6, "water": 0, "heat": 6, "elec": 0, "gas": 0, "other": 6}
    ]

    removeType(list, "water")

    assert list == [
        {"id": 1, "water": 0, "heat": 1, "elec": 1, "gas": 1, "other": 0},
        {"id": 2, "water": 0, "heat": 0, "elec": 2, "gas": 0, "other": 0},
        {"id": 3, "water": 0, "heat": 3, "elec": 0, "gas": 3, "other": 0},
        {"id": 4, "water": 0, "heat": 4, "elec": 4, "gas": 4, "other": 4},
        {"id": 5, "water": 0, "heat": 0, "elec": 5, "gas": 0, "other": 0},
        {"id": 6, "water": 0, "heat": 6, "elec": 0, "gas": 0, "other": 6}
    ]

    removeType(list, "other")

    assert list == [
        {"id": 1, "water": 0, "heat": 1, "elec": 1, "gas": 1, "other": 0},
        {"id": 2, "water": 0, "heat": 0, "elec": 2, "gas": 0, "other": 0},
        {"id": 3, "water": 0, "heat": 3, "elec": 0, "gas": 3, "other": 0},
        {"id": 4, "water": 0, "heat": 4, "elec": 4, "gas": 4, "other": 0},
        {"id": 5, "water": 0, "heat": 0, "elec": 5, "gas": 0, "other": 0},
        {"id": 6, "water": 0, "heat": 6, "elec": 0, "gas": 0, "other": 0}
    ]


def test_replace():
    ap = {"id": 1, "water": 0, "heat": 0, "elec": 0, "gas": 12, "other": 24}

    setAmount(ap, "heat", 22)
    assert ap == {"id": 1, "water": 0, "heat": 22, "elec": 0, "gas": 12, "other": 24}

    setAmount(ap, "gas")
    assert ap == {"id": 1, "water": 0, "heat": 22, "elec": 0, "gas": 0, "other": 24}


def test_isNumber():
    assert isNumber("12") == True
    assert isNumber("-34") == True
    assert isNumber("455") == True
    assert isNumber("23a") == False
    assert isNumber("asdf") == False
    assert isNumber("a123") == False


def test_isType():
    assert isType("gas") is True
    assert isType("heat") is True
    assert isType("water") is True
    assert isType("other") is True
    assert isType("elec") is True
    assert isType("asdf") is False
    assert isType("gass") is False


def test_sum():
    list = [
        {"id": 1, "water": 1, "heat": 1, "elec": 1, "gas": 1, "other": 0},
        {"id": 2, "water": 2, "heat": 0, "elec": 2, "gas": 10, "other": 0},
        {"id": 3, "water": 0, "heat": 3, "elec": 0, "gas": 3, "other": 0}
    ]

    assert sum(list, "water") == 3
    assert sum(list, "heat") == 4
    assert sum(list, "elec") == 3
    assert sum(list, "gas") == 14
    assert sum(list, "other") == 0


def test_filterType():

    list = [
        {"id": 1, "water": 1, "heat": 1, "elec": 1, "gas": 1, "other": 0},
        {"id": 2, "water": 2, "heat": 0, "elec": 2, "gas": 0, "other": 0},
        {"id": 3, "water": 0, "heat": 3, "elec": 0, "gas": 3, "other": 0},
        {"id": 4, "water": 4, "heat": 4, "elec": 4, "gas": 4, "other": 4},
        {"id": 5, "water": 5, "heat": 0, "elec": 5, "gas": 0, "other": 0},
        {"id": 6, "water": 0, "heat": 6, "elec": 0, "gas": 0, "other": 6}
    ]

    filterType(list,"heat")

    assert list == [
        {"id": 1, "water": 0, "heat": 1, "elec": 0, "gas": 0, "other": 0},
        {"id": 2, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0},
        {"id": 3, "water": 0, "heat": 3, "elec": 0, "gas": 0, "other": 0},
        {"id": 4, "water": 0, "heat": 4, "elec": 0, "gas": 0, "other": 0},
        {"id": 5, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0},
        {"id": 6, "water": 0, "heat": 6, "elec": 0, "gas": 0, "other": 0}
    ]


def test_filterAmount():
    list = [
        {"id": 1, "water": 1, "heat": 100, "elec": 1, "gas": 1, "other": 0},
        {"id": 2, "water": 2, "heat": 0, "elec": 2, "gas": 0, "other": 0},
        {"id": 3, "water": 0, "heat": 300, "elec": 0, "gas": 3, "other": 0},
        {"id": 4, "water": 4, "heat": 4, "elec": 4, "gas": 4, "other": 4},
        {"id": 5, "water": 5, "heat": 0, "elec": 5, "gas": 0, "other": 0},
        {"id": 6, "water": 0, "heat": 6, "elec": 0, "gas": 0, "other": 6}
    ]

    filterAmount(list, 100)

    assert list == [
        {"id": 1, "water": 0, "heat": 100, "elec": 0, "gas": 0, "other": 0},
        {"id": 2, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0},
        {"id": 3, "water": 0, "heat": 300, "elec": 0, "gas": 0, "other": 0},
        {"id": 4, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0},
        {"id": 5, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0},
        {"id": 6, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0}
    ]


def test_sortApartment():
    apartments = [
        {"id": 1, "water": 0, "heat": 100, "elec": 0, "gas": 0, "other": 0},
        {"id": 2, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0},
        {"id": 3, "water": 0, "heat": 0, "elec": 300, "gas": 0, "other": 0}
    ]

    assert sortApartment(apartments) == [
        [2, 0],
        [1, 100],
        [3, 300]
    ]

    apartments = [
        {"id": 1, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0},
        {"id": 2, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0},
        {"id": 3, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0}
    ]

    assert sortApartment(apartments) == [
        [1, 0],
        [2, 0],
        [3, 0]
    ]

def test_sortType():
    apartments = [
        {"id": 1, "water": 0, "heat": 100, "elec": 0, "gas": 0, "other": 0},
        {"id": 2, "water": 0, "heat": 0, "elec": 0, "gas": 0, "other": 0},
        {"id": 3, "water": 0, "heat": 0, "elec": 300, "gas": 0, "other": 0}
    ]

    assert sortType(apartments) == [
        ["water", 0],
        ["gas", 0],
        ["other", 0],
        ["heat", 100],
        ["elec", 300]
    ]

    apartments = [
        createExpense(1),
        createExpense(2),
        createExpense(3)
    ]

    assert sortType(apartments) == [
        ["water", 0],
        ["heat", 0],
        ["elec", 0],
        ["gas",0],
        ["other", 0]
    ]


def test_maxi():
    ap = {"id": 2, "water": 0, "heat": 10, "elec": 0, "gas": 20, "other": 0}
    assert maxi(ap) == [["gas", 20]]

    ap = {"id": 2, "water": 0, "heat": 100, "elec": 0, "gas": 20, "other": 0}
    assert maxi(ap) == [["heat", 100]]

    ap = {"id": 2, "water": 1, "heat": 1, "elec": 0, "gas": 0, "other": 0}
    assert maxi(ap) == [["water", 1], ["heat", 1]]

def test_undo():

    #-------- add

    e1 = createExpense(1)
    e2 = createExpense(2)
    e3 = createExpense(3)

    undoList = []

    aps = [ e1, e2, e3 ]
    copy = deepcopy(aps)
    undoList.append(copy)
    addExpense(aps[1],"water",10)

    e1New = e1
    setAmount(e1New,"water",10)


    assert aps == [ e1New, e2, e3 ]

    undo(aps,undoList)

    assert aps == copy

    #-------- remove

    e1 = createExpense(1,1,1,1,1)
    e2 = createExpense(2,1,1,1,1)
    e3 = createExpense(3,1,1,1,1)

    undoList = []
    aps = [ e1, e2, e3 ]

    copy = deepcopy(aps)
    undoList.append(copy)

    removeApart(aps,1,1)

    e1New = createExpense(1)


    assert aps == [ e1New, e2, e3 ]

    undo(aps,undoList)

    assert aps == copy

    #------- filter

    e1 = createExpense(1)
    e2 = createExpense(2)
    e3 = createExpense(3)

    undoList = []
    aps = [ e1, e2, e3 ]

    copy = deepcopy(aps)
    undoList.append(copy)

    filterType(aps,"water")



    e1New = e1
    e2New = e2
    e3New = e3
    setAmount(e1New, "water")
    setAmount(e2New, "water")
    setAmount(e3New, "water")


    assert aps == [ e1New, e2New, e3New ]

    undo(aps,undoList)

    assert aps == copy

    #------ replace

    e1 = createExpense(1, 1, 1, 1, 1)
    e2 = createExpense(2, 1, 1, 1, 1)
    e3 = createExpense(3, 1, 1, 1, 1)

    undoList = []

    aps = [e1, e2, e3]
    e1New = e1
    setAmount(e1New,"water",10)

    copy = deepcopy(aps)
    undoList.append(copy)

    replace(aps[0],"water",10)

    assert aps == [e1New, e2, e3]

    undo(aps, undoList)

    assert aps == copy

    #-------- create and add to list

    e1 = createExpense(1, 1, 1, 1, 1)
    e2 = createExpense(2, 1, 1, 1, 1)
    e3 = createExpense(3, 1, 1, 1, 1)

    undoList = []

    aps = [e1, e2, e3]

    copy = deepcopy(aps)
    undoList.append(copy)

    createAddExpense(12,"water",12,aps)

    e4 = createExpense(12)
    setAmount(e4,"water",12)

    assert aps == [e1, e2, e3, e4]

    undo(aps, undoList)

    assert aps == copy


def run_tests():

    test_createExpense()
    test_getAmount()
    test_getId()
    test_setAmount()
    test_removeApart()
    test_removeType()
    test_getApIdList()
    test_isNumber()
    test_isType()
    test_replace()
    test_sum()
    test_filterType()
    test_filterAmount()
    test_sortApartment()
    test_sortType()
    test_maxi()
    test_undo()
