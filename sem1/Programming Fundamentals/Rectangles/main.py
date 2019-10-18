'''
Created on 14 Nov 2018

@author: stiub

Rectangle:
    - ident ( int positive)
    - hl (x0,y0) positive
    - lr (x1,y1) positive
    -color ( nonempty string )
    -value ( float, positive )

surface = | y1-y0 | * | x1 - x0 |

1. add parcel to app

2. if two rectangles overlap 
    replace them by one rectangle
    color -  grey
    the value will become nv = ( Va*Sa + Vb-Sb )/ Sa + Sb

3. having an amount of money given by the user 
        give the list of the red colored areas 
            whose values you can afford to buy
            sorted according to their per unit price ( Value of a / Surface of a )

'''
from tests import run_tests
from functions import *
from ui import *

def run_app():
    
    lst = [
            { "id": 1, "hl": [1,1], "lr": [2,2], "color": "red", "value": 11.5 },
            { "id": 2, "hl": [4,4], "lr": [5,5], "color": "white", "value": 2.1 },
            { "id": 3, "hl": [6,6], "lr": [8,8], "color": "black", "value": 2.4 },
            { "id": 4, "hl": [1,1], "lr": [2,2], "color": "red", "value": 50.5 },
            { "id": 5, "hl": [1,1], "lr": [2,2], "color": "red", "value": 1.5 }
        ]
    
    while True:
        print_menu()
        cmd = input(">>")
        
        if cmd == "add":
            ui_add(lst)
        elif cmd == "list":
            print_list(lst)
        elif cmd == "buy":
            ui_buy(lst)
        elif cmd == "exit":
            return
        else: print("Invalid command!")
    
run_tests()
run_app()