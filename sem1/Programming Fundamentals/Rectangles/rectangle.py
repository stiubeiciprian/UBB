'''
Created on 14 Nov 2018

@author: stiub
'''

def createRectangle( ident, x0, y0, x1 , y1, color, value ):
    
    '''
    Function that creates a rectangle.
    In: id - int, positive
        x0,y0 - int, positive, coordinates of higher left corner
        x1,y1 - int, positive, coordtinates of lower right corner
        color - nonempty string
        value - float, positive
    Out: rectangle
    '''
    
    return { "id": ident, "hl": [x0, y0], "lr": [x1, y1], "color": color, "value": value }


'''
Getters
'''

def getId(r): 
    return r["id"]

def getHl(r): 
    return r["hl"]

def getLr(r): 
    return r["lr"]

def getColor(r): 
    return r["color"]

def getValue(r): 
    return r["value"]

'''
Setters
'''

def setId(r, n): 
    r["id"] = n

def setHl(r, n): 
    r["hl"]  = n

def setLr(r, n): 
    r["lr"]  = n

def setColor(r, n): 
    r["color"]  = n

def setValue(r, n): 
    r["value"]  = n