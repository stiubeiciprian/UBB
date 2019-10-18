'''
Created on 14 Nov 2018

@author: stiub
'''
from rectangle import getId, getHl

def validateRectangle(ident, x0, y0, x1, y1, color, value):
    
    error_str=""
    valid = True
       
    try:
        if int(ident) < 0:
            error_str.append("Id cant be negative!\n")
            valid = False
    except:
        error_str.append("Id must be an integer!\n")
        valid = False

    if color == "":
        valid = False
        error_str.append("color cant be empty string\n")
    
    if not valid:
        raise error_str
    