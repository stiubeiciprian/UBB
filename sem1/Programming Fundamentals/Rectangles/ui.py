'''
Created on 14 Nov 2018

@author: stiub
'''
from rectangle import *
from validator import *
from functions import *

def print_menu():
    '''
    Function that prints menu text.
    In:-
    Out:-
    '''
    s = "Available commands\n"
    s+= "\tadd- adds parcel to list\n"
    s+= "\tlist - print list of parcels\n"
    s+= "\tbuy - print list of affordable red parcels\n"
    s+= "\texit\n"
    
    print(s)
    
def print_list(lst):
    
    for elem in lst:
        print(toStr(elem))
    
def ui_add(lst):
    '''
    Function that adds a new given rectangle r to the list of rectangles.
    In: lst - list of rectangles
    Out: -
    Post: r is added to the rectangles
    '''
    
    ident = input("Enter id:")
    x0 = input("Enter x0:")
    y0 = input("Enter y0:")
    x1 = input("Enter x1:")
    y1 = input("Enter y1:")
    color = input("Enter color:")
    value = input("Enter value:")
    
    validateRectangle(ident, x0, y0, x1, y1, color, value)
    
    r = createRectangle(int(ident), int(x0), int(y0), int(x1), int(y1), color, float(value))
    
    addToList(lst,r)
    
def ui_buy(lst):
    '''
    Function that prints all afordable parcels with color red sorted by thei per unit price.
    In: lst - list of all parcels
    Out: -
    '''
    
    money = float(input("Enter amount of money:"))
    
    newLst = buyParcel(lst, money, "red")
    
    newLst = sorted(newLst, key=getPricePerUnit)
    
    print_list(newLst)
    
    return newLst
    
    