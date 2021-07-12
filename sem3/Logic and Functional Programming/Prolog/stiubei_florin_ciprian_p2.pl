/* Problem 7
 * a) Determine the position of the maximal element of a linear list.
 * Eg.: maxpos([10,14,12,13,14], L) produces L = [2,5].
 *
 *  maximum(A:integer, B:integer)
 *    A , A >= B
 *    B , A < B
 *
 *  findMax(L:list)
 *    0 , L is an empty list
 *    l1 , L has one element
 *    maximum(l1, findMax(l2..ln)) , L > 2
 *
 *
 *  findMaxPosition(L:list, Max:integer, Pos:integer)
 *    [], L is an empty list
 *    Pos U findMaxPosition(l2..ln,Max,Pos+1) , element on position Pos is equal to Max
 *    findMaxPosition(l2..ln,Max,Pos+1) , otherwise
 *
 */

%maximum(A:integer, B:integer, R:integer)
%(i,i,o)
maximum(A,B,R):-
    A>=B,
    R is A.
maximum(A,B,R):-
    A<B,
    R is B.

%findMax(L:list,R:integer)
%(i,o)
findMax([],0).
findMax([E],E).
findMax([H|T],R):-
    T=0,
    R is H.
findMax([H|T],R):-
    findMax(T,Rs),
    maximum(H,Rs,R).

%findMaxPosition(L:list, Max:integer, Pos:integer, R:list)
%(i,i,i,o)
findMaxPosition([],_,_,[]).
findMaxPosition([H|T],Max,Pos,[Pos|Rs]):-
    H=:=Max,
    Pos1 is Pos+1,
    findMaxPosition(T,Max,Pos1,Rs).
findMaxPosition([H|T],Max,Pos,Rs):-
    H=\=Max,
    Pos1 is Pos+1,
    findMaxPosition(T,Max,Pos1,Rs).

%findMaxPositionMain(L:list,R:list)
%(i,o)
findMaxPositionMain(L,R):-
    findMax(L,Max),
    findMaxPosition(L,Max,1,R).


/* b) For a heterogeneous list, formed from integer numbers and list of numbers, replace every * sublist with the position of the maximum element from that sublist.
 * [1, [2, 3], [4, 1, 4], 3, 6, [7, 10, 1, 3, 9], 5, [1, 1, 1], 7] =>
 * [1, [2], [1, 3], 3, 6, [2], 5, [1, 2, 3], 7]
 *
 * replace(L:list)
 *  [] , L is an empty list
 *  l1 U replace(l2..ln), l1 is not a list
 *  findMaxPositionMain(l1) U replace(l2..ln), l1 is a list
 */

%replace(L:list,R:list)
%(i,o)
replace([],[]).
replace([H|T],[H|Rs]):-
    not(is_list(H)),
    replace(T,Rs).
replace([H|T],[Max|Rs]):-
    is_list(H),
    findMaxPositionMain(H,Max),
    replace(T,Rs).
