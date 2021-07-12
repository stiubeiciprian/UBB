;;; an n-ary tree can be memorized as a linear list where each node is followed by the number of children.
;;; write a function to return the kth child (as a list) of an n-ary tree.
;;; ex: tree (A 5 B 2 E 0 F 3 G 0 H 0 I 0 C 1 J 1 K 2 L 0 M 0 D 4 N 0 O 0 P 2 R 0 S 1 T 0 Q 0 U 0 V 1 Z 2 T 0 W 0)
;;; k = 3 => (D 4 N 0 O 0 P 2 R 0 S 1 T 0 Q 0)
;;; k = 5 => (V 1 Z 2 T 0 W 0)


#|
    getKChildRec(tree, childNumber, nodes, edges, k)
    nil, if tree is empty
    '(root rootEdges), if nodes = edges + rootEdges AND childNumber = k
    '(root rootEdges) U getKChildRec(nextTree childNumber nodes+1 edges+rootEdges k), if childNumber = k
    getKChildRec(nextTree childNumber+1 0 0 k), if nodes = edges + rootEdges
    getKChildRec(nextTree childNumber nodes+1 edges+rootEdges k), otherwise

|#
(defun getKChildRec (tree childNumber nodes edges k)
    (cond
        ((null tree) nil)
        ((and (= nodes (+ edges (cadr tree))) (= childNumber k))    (list (car tree) (cadr tree)))
        ((= childNumber k)  (append 
                                (list (car tree) (cadr tree)) 
                                (getKChildRec (cddr tree) childNumber (+ 1 nodes) (+ edges (cadr tree)) k)
                            )
        )
        ((= nodes (+ edges (cadr tree)))    (getKChildRec (cddr tree) (+ 1 childNumber) 0 0 k))
        (t (getKChildRec (cddr tree) childNumber (+ 1 nodes) (+ edges (cadr tree)) k))
    )
)

(defun getKChild (tree k)
    (getKChildRec (cddr tree) 1 0 0 k)
)

(print (getKChild '(A 5 B 2 E 0 F 3 G 0 H 0 I 0 C 1 J 1 K 2 L 0 M 0 D 4 N 0 O 0 P 2 R 0 S 1 T 0 Q 0 U 0 V 1 Z 2 T 0 W 0) 3 ))

;;; given a nonlinear list containing both numerical and non-numerical atoms compute the gcd
;;; of the odd numbers from the even levels (the superficial level is odd)
;;; (A B 12 (9 D (A F (75 B) D (45 F) 1) 15 ) C 9) => 3

(defun mygcd (a b)
    (cond
        ((= b 0) a)
        (t (mygcd b (mod a b)))
    )
)

(defun getGcdRec (lst tempGcd)
    (cond
        ((null lst) tempGcd)
        (t (getGcdRec (cdr lst) (mygcd tempGcd (car lst))))
    )
)

(defun getGcd (lst)
    (getGcdRec lst (car lst))
)

(defun solveRec (lst level)
    (cond
        ((and (and (numberp lst) (oddp lst)) (evenp level)) (list lst))
        ((atom lst) nil)
        (t (mapcan #'(lambda (a) (solveRec a (+ level 1))) lst))
    )
)

(defun solve (lst)
    (getGcd (solveRec lst 0))
)

;;; given a non-linear list replace every non-numerical atom with the number of occurences on its level

(defun countOcc (lst elem)
    (cond
        ((null lst) 0)
        ((equal (car lst) elem) (+ 1 (countOcc (cdr lst) elem)))
        (t (countOcc (cdr lst) elem))
    )
)

(defun replaceAtoms (x lst)
    (cond
        ((null x) nil)
        ((and (atom (car x)) (numberp (car x))) (cons (car x) (replaceAtoms (cdr x) lst)))
        ((atom (car x)) (cons (countOcc lst (car x)) (replaceAtoms (cdr x) lst)))
        (t (cons (replaceAtoms (car x) (car x)) (replaceAtoms (cdr x) lst)))
    )
)

(defun solveAtoms (lst)
    (replaceAtoms lst lst)
)

(print (car nil))