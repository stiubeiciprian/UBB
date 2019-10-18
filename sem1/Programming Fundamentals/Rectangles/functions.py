'''
Created on 14 Nov 2018

@author: stiub
'''
from rectangle import *

def getIds(lst):
    
    '''
    Function that returns all the ids of the parcels in the list.
    '''
    id_lst = []
    
    for r in lst:
        id_lst.append(getId(r))
        
    return id_lst

def getSurface(r):
    '''
    Function that returns the surface or a rectangle r.
    In: r -rectangle
    Out: surface - surface or rectangle r
    '''
    x0 = getHl(r)[0]
    y0 = getHl(r)[1]
    
    x1 = getLr(r)[0]
    y1 = getLr(r)[1]
    
    return abs(x0-x1)*abs(y0-y1)

def toStr(r):
    '''
    Function that returns all information about rectangle r in a string.
    In: r - rectangle
    Out: string containing all information about r
    '''
    return " Id:" + str(getId(r)) + " x0:" + str(getHl(r)[0]) + " y0:" + str(getHl(r)[1]) + " x1:" + str(getLr(r)[0]) + " y1:" + str(getLr(r)[1]) + " color:" + str(getColor(r)) + " value:" + str(getValue(r))

def addToList(lst, r):
    '''
    Function that adds a rectangle to the list.
    In: lst - list of rectangles, lst = [ r1, r2, ... rn ]
        r - rectangle
    Out: -
    Post: updated lst , lst = [ r1, r2, ... rn, r ]
    '''
    
    lst.append(r)

def buyParcel(lst, money, color):
    '''
    Function that returns a list of parcels with price<=money and the given color.
    '''
    
    newLst = []
    
    for r in lst:
        if getColor(r) == color and getValue(r) <= money:
            newLst.append(r)

    return newLst


def getPricePerUnit(r):
    '''
    Function that returns the price per unit.
    In: r - rectangle
    Out: p = value of r / surface of r , - float
    '''
    return getValue(r)/getSurface(r)