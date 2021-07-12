#|
    9.
        a) Write a function that merges two sorted linear lists and keeps double values.
        b) Write a function to replace an element E by all elements of a list L1 at all levels of a given list L.
        c) Write a function to determines the sum of two numbers in list representation, and returns the 
        corresponding decimal number, without transforming the representation of the number from list to number.
        d) Write a function to return the greatest common divisor of all numbers in a linear list
|#

#| a)
    mergeSortedLists(f:list, s:list)
        f, if s is an empty list
        s, if f is an empty list
        f1 U mergeSortedLists(f2..fn, s), if f1 <= s1
        s1 U mergeSortedLists(f, s2..sm), if f1 > s1
|#
(defun mergeSortedLists (firstList secondList)
    (cond 
        ((null secondList) firstList)
        ((null firstList) secondList)
        ((<= (car firstList) (car secondList)) (cons (car firstList) (mergeSortedLists (cdr firstList) secondList)))
        ((> (car firstList) (car secondList)) (cons (car secondList) (mergeSortedLists firstList (cdr secondList))))
    )
)

(print (mergeSortedLists (LIST 1 2 3) (LIST 1 2 2 3 4)))

#| b)
    replaceElement(e:atom, l:list, L:list)
        empty list, if L is an empty list
        replaceElement(e l L1) U replaceElement(e l L2..Ln), if L1 is a list
        l U replaceElement(e,l,L2..Ln, if L1 = e
        L1 U replaceElement(e,l,L2..Ln), if L1 != e
|#

(defun replaceElement (e replacementList inputList)
    (cond
        ((null inputList) NIL)
        ((listp (car inputList)) 
            (cons 
                (replaceElement e replacementList (car inputList)) 
                (replaceElement e replacementList (cdr inputList))
           ))

        ((equal (car inputList) e) 
            (append 
                replacementList 
                (replaceElement e replacementList (cdr inputList))
        ))

        (t (cons 
                (car inputList) 
                (replaceElement e replacementList (cdr inputList))
        ))
    )
)

;(print (replaceElement 3 (LIST 99 99) (LIST (LIST 1 3) 1 2 3 1 2 3)))

#| c)
    addListNumbersRec(X:list, Y:list, R:integer)
        addListNumbersRec(X2..Xn, Y1..Ym, R*10 + X1), if n > m
        addListNumbersRec(X1..Xn, Y2..Ym, R*10 + Y1), if n < m
        R, if X or Y is an empty list
        addListNumbersRec(X2..Xn, Y2..Yn, R*10 + X1 + Y1), otherwise
|# 

(defun addListNumbersRec(X Y R)
    (cond
        ((> (length X) (length Y)) (addListNumbersRec (cdr X) Y (+ (* R 10) (car X))))
        ((< (length X) (length Y)) (addListNumbersRec X (cdr Y) (+ (* R 10) (car Y))))
        ((or (null X) (null Y)) R)
        (t (addListNumbersRec (cdr X) (cdr Y) (+ (* R 10) (car X) (car Y))))
    )
)

(defun addListNumbers(X Y)
    (addListNumbersRec X Y 0)
)

(print (addListNumbers (LIST 1 2 3 4) (LIST 5 6 6)))
(print (addListNumbers (LIST ) (LIST 5 6 6)))
(print (addListNumbers (LIST 1) (LIST 9 9)))

#| d)
    greatestCommonDivisor(x:integer, y:integer)
        x, if y = 0 
        greatestCommonDivisor(y, x%y), otherwise
|#
(defun greatestCommonDivisor(x y)
    (cond 
        ((equal y 0) x)
        (t (greatestCommonDivisor y (mod x y)))
    )
)

#|
    greatestCommonDivisorList(L:list)
        1 , if L is empty
        L1, if L2..Ln is empty
        greatestCommonDivisor(L1, greatestCommonDivisorList(L2..Ln)), otherwise
|#
(defun greatestCommonDivisorList(l)
    (cond 
        ((null l) 1)
        ((null (cdr l)) (car l))
        (t (greatestCommonDivisor (car l) (greatestCommonDivisorList (cdr l))))
    )
)


;(print (greatestCommonDivisorList (list 4 16 8 18 5)))
;(print (greatestCommonDivisorList (list )))