#|
    Write recursive Lisp functions for the following problems (optionally, you may use MAP functions):

        A binary tree is memorised in the following two ways:
            (node no-subtrees list-subtree-1 list-subtree-2 ...) (1)
            (node (list-subtree-1) (list-subtree-2) ...) (2)
            
        As an example, the tree
               A
              / \
             B   C
                / \
               D   E
        is represented as follows:

        (A 2 B 0 C 2 D 0 E 0) (1)
        (A (B) (C (D) (E))) (2)

    1. For a given tree of type (1) return the path from the root node to a certain given node X.
|#

#|
    addToEnd(e:element, l:list)
        list(e), if l is null
        addToEnd(l2..ln, e), otherwise
|#
(defun addToEnd (e l)
    (cond
        ((null l) (list e))
        (t (cons (car l) (addToEnd e (cdr l))))
    )
)



#|
    getLeftSubtree(tree:list, nodes:integer, edges:integer)
        nil, if tree is empty
        root U rootEdges, if nodes = edges + rootEdges
        root, rootEdges U getLeftSubtree(tree3..treeN, nodes+1, edges+rootEdges), otherwise
|#
(defun getLeftSubtree (tree nodes edges)
    (cond
        ((null tree) nil)
        ((= nodes (+ edges (cadr tree))) (list (car tree) (cadr tree)))
        (t (append (list (car tree) (cadr tree)) (getLeftSubtree (cddr tree) (+ 1 nodes) (+ (cadr tree) edges))))
    )
)

#|
    getLeft(tree:list)
        getLeftSubtree(tree3..treeN, 0, 0)
|#
(defun getLeft (tree)
    (getLeftSubtree (cddr tree) 0 0)
)




#|
    getRightSubtree(tree:list, nodes:int, edges:int)
        nil, if tree is null
        tree3..treeN , if nodes = edges + rootEdges
|#
(defun getRightSubtree (tree nodes edges)
    (cond
        ((null tree) nil)
        ((= nodes (+ edges (cadr tree))) (cddr tree))
    )
)

#|
    getRight(tree:list)
        getRightSubtree(tree3..treeN, 0, 0)
|#
(defun getRight (tree)
    (getRightSubtree (cddr tree) 0 0)
)




#|
    getPathToNode(tree:list, node:node, resultPath:list)
        nil, if tree is empty
        node U resultPath, if node = root
        getPathToNode(getLeft(tree), node, root U resultPath), if its result its not empty
        getPathToNode(getRight(tree), node, root U resultPath), if its result is not empty
        nil, otherwise
|#
(defun getPathToNode (tree node resultPath)
    (cond
        ((null tree) nil)
        ((equal (car tree) node) (addToEnd node resultPath))
        ((not (null (getPathToNode (getLeft tree) node (addToEnd (car tree) resultPath)))) 
            (getPathToNode (getLeft tree) node (addToEnd (car tree) resultPath))
        )
        ((not (null (getPathToNode (getRight tree) node (addToEnd (car tree) resultPath)))) 
            (getPathToNode (getRight tree) node (addToEnd (car tree) resultPath))
        )
        (t nil)
    )
)

#|
    getPathToNodeMain(tree:list, node:node)
        getPathToNode(tree, node, nil)
|#
(defun getPathToNodeMain (tree node)
    (getPathToNode tree node nil)
)


(setq exampleTree '(A 2 B 0 C 2 D 0 E 0))
(print (getPathToNodeMain exampleTree 'e))
(print (getPathToNodeMain exampleTree 'b))
(print (getPathToNodeMain exampleTree 'd))
(print (getPathToNodeMain exampleTree 'a))
(print (getPathToNodeMain exampleTree 'q))