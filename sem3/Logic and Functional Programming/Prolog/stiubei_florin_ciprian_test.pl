/**
 * PROLOG 4: Se da o lista de numere intregi. Scrieti un predicat care
 * sa stearga toate elementele care sunt patrat perfect.
 *
 * isPerfectSquare(N)
 *   true, if sqrt(N)*sqrt(N) = N
 *   false, otherwise
 *
 * isPerfectSquare(1).
 * isPerfectSquare(0).
 * isPerfectSquare(16).
 *
 * isPerfectSquare(-1).
 * isPerfectSquare(7).
 */
%isPerfectSquare(N:integer)
%(i)
isPerfectSquare(N):-
    N >= 0,
    sqrt(N)*sqrt(N)=:=N.

/**
 * removePerfSquares(L)
 *   empty list, if list is empty
 *   l1 U removePerfSquares(l2..ln), if l1 is not a perfect square
 *   removePerfSquares(l2..ln), if l1 is a perfect square
 *
 * [3,9,2,5,16,4,3,49,0,6] => [3,2,5,3,6]
 *
 * removePerfSquares([3,9,2,5,16,4,3,49,0,6],[3,2,5,3,6]).
 * removePerfSquares([],[]).
 * removePerfSquares([5,7,8],[5,7,8]).
 * removePerfSquares([-1,-4,0,6,4],[-1,-4,6]).
 */

%removePerfSquares(L:list, R:list)
%(i,o)
removePerfSquares([],[]).
removePerfSquares([H|T],[H|R]):-
    not(isPerfectSquare(H)),
    removePerfSquares(T,R).
removePerfSquares([H|T],R):-
    isPerfectSquare(H),
    removePerfSquares(T,R).
