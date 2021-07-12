#| 
LISP 1 Dandu-se o lista liniara, sa se stearga toate secventele de valori numerice NEconsecutive. De exemplu:
(1 2 c 4 6 7 8 i 10 11 j) --> (1 2 c 6 7 8 i j)
|#


#|
    deleteValues(lst:list)
        nil, if list is empty
        deleteValues(l2..ln), if l1 is a number and belongs to a consecutive sequence
        l1 U deleteValues(l2..ln), otherwise
|#
(defun deleteValues (lst)
    (cond
        ((null lst) nil)
        ((and (numberp (car lst))   (not (consecutive (cdr lst) (car lst))))
            (deleteValues (cdr lst))
        )
        (t (cons 
                (car lst) 
                (deleteValues (cdr lst))
            )
        )
    )
)



(defun consecutive (lst e)
    (cond 
        ((null lst) nil)
        ((equal (car lst) (+ e 1)) 1)
        (t nil)
    )
)

 (print (deleteValues '(1 2 c 4 6 7 8 i 10 11 j)))

;; #|
;; Sau: Cerinta minimala pentru 5: Stergerea unui element E dintr-o lista L.
;; |#
;; #|
;;     deleteElement(lst:list e:element)
;;         nil, if list is empty
;;         deleteElement(l1 e) U deleteElement(l2..ln e), if l1 is list
;;         l1 U deleteElement(l2..ln), if l1 != e
;;         deleteElement(l2..ln), if l1 = e

;; |#
;; (defun deleteElement(lst e)
;;     (cond 
;;         ((null lst) nil)
;;         ((listp (car lst))
;;             (cons
;;                 (deleteElement (car lst) e) 
;;                 (deleteElement (cdr lst) e)
;;             )
;;         )
;;         ((not (equal (car lst) e)) 
;;             (cons
;;                 (car lst)
;;                 (deleteElement (cdr lst) e)
;;             )
;;         )
;;         ((equal (car lst) e) (deleteElement (cdr lst) e))
        
;;     )
;; )

;; (print (deleteElement '(1 2 c (1 2 1) 6 7 (1 (1 2)) i 1 j) 1))