'''
Created on 14 Nov 2018

@author: stiub
'''

from rectangle import *
from functions import *
from validator import validateRectangle


def test_getters():
    
    ident = 1
    x0 = 1
    y0 = 1
    x1 = 2
    y1 = 2
    color = "red"
    value = 11.5
    
    r = { "id": ident, "hl": [x0, y0], "lr": [x1, y1], "color": color, "value": value }
    
    assert r["id"] == getId(r)
    assert r["hl"] == getHl(r)
    assert r["lr"] == getLr(r)
    assert r["color"] == getColor(r)
    assert r["value"] == getValue(r)
    
    assert getSurface(r) == abs(x0-x1)*abs(y0-y1)
    
    assert getPricePerUnit(r) == getValue(r)/getSurface(r)
    
    
def test_createRectangle():
    
    ident = 1
    x0 = 1
    y0 = 1
    x1 = 2
    y1 = 2
    color = "red"
    value = 11.5
    
    r = createRectangle(ident, x0, y0, x1, y1, color, value )
    
    assert getId(r) == ident
    assert getHl(r) == [x0,y0]
    assert getLr(r) == [x1,y1]
    assert getValue(r) == value
    assert getColor(r) == color
    
def test_validateRectangle():
   
    bident = -1
    bx0 = -1
    by0 = -1
    bx1 = -2
    by1 = -2
    bcolor = ""
    bvalue = -11.5
    
    try:
        validateRectangle(bident, bx0, by0, bx1, by1, bcolor, bvalue)
        assert False
    except:
        pass

def test_addToList():
    
    lst= []
    
    ident = 1
    x0 = 1
    y0 = 1
    x1 = 2
    y1 = 2
    color = "red"
    value = 11.5
    
    r = createRectangle(ident, x0, y0, x1, y1, color, value )
    
    addToList(lst, r)
    
    assert lst == [r]
    
def test_buy():
    
    lst = [
            { "id": 1, "hl": [1,1], "lr": [2,2], "color": "red", "value": 11.5 },
            { "id": 4, "hl": [1,1], "lr": [2,2], "color": "red", "value": 11.5 },
            { "id": 2, "hl": [4,4], "lr": [5,5], "color": "white", "value": 2.1 },
            { "id": 3, "hl": [6,6], "lr": [8,8], "color": "black", "value": 2.4 }
        ]
    
    assert buyParcel(lst, 20.0, "red") == [
        { "id": 1, "hl": [1,1], "lr": [2,2], "color": "red", "value": 11.5 },
        { "id": 4, "hl": [1,1], "lr": [2,2], "color": "red", "value": 11.5 }
        
        ]


def run_tests():
    test_getters()
    test_createRectangle()
    test_validateRectangle()
    test_addToList()
    test_buy()
    
    