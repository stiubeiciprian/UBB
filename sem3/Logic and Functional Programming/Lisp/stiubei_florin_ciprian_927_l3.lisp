#|
8. Write a function to determine the number of nodes on the level k from a n-tree represented as follows:
(root list_nodes_subtree1 ... list_nodes_subtreen)
Eg: tree is (a (b (c)) (d) (e (f))) and k=1 => 3 nodes
|#


#|
    countKLevelNodes(tree:list, k:int, currentLevel:int)
        1, if tree is atom and k = currentLevel
        0, if tree is atom and k!= currentLevel
        sum(countKLevelNodes())
|#
(defun countKLevelNodes (tree k currentLevel)
    (cond 
        ((and (atom tree) (equal k currentLevel)) 1)
        ((and (atom tree) (not (equal k currentLevel))) 0)
        (t (apply '+ (mapcar #'(lambda (x) (countKLevelNodes x k (+ currentLevel 1))) tree)))
    )
)

#|
    countKLevelNodesMain(tree:list, k:int)
        countKLevelNodes(tree, k, -1)
|#
(defun countKLevelNodesMain (tree k)
    (countKLevelNodes tree k -1)
)

(print '(A (B (C)) (D) (E (F))))
(print (countKLevelNodesMain '(A (B (C)) (D) (E (F))) 0))
(print (countKLevelNodesMain '(A (B (C)) (D) (E (F))) 1))
(print (countKLevelNodesMain '(A (B (C)) (D) (E (F))) 2))
