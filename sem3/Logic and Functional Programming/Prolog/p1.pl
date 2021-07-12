%a)  Write a predicate to determine the lowest common multiple of a list formed from integer numbers.

/*
 * gcd(a,b)
 *   a , b = 0
 *   gcd(a%b) , a > b
 *   gcd(b%a) , a <= b
 */


%gcd(A:integer, B:integer, R:integer)
%(i,i,o)
gcd(A,0,A).
gcd(A,B,R):-
    A>B,
    gcd(B,mod(A,B),R1),
    R is R1.
gcd(A,B):-
    A=<B,
    gcd(A,mod(B,A)).


/*
 * leastCommonMultiple(L)
 *   1 , L = []
 *   l1*leastCommonMultiple(l2..ln)/gcd(l1, leastCommonMultiple(l2..ln))
 */

%leastCommonMultiple(L:list, R:integer)
%(i,o)
leastCommonMultiple([],1).
leastCommonMultiple([H|T],R):-
    leastCommonMultiple(T,Rs),
    R is H*Rs/gcd(H,Rs).

%b)  Write a predicate to add a value v after 1-st, 2-nd, 4-th, 8-th, … element in a list.

/*
 * powerOfTwo(N)
 *   true , N=1
 *   powerOfTwo(N/2) , N>1
 */


%powerOfTwo(N:integer)
%(i)
powerOfTwo(1).
powerOfTwo(N):-
    N > 1,
    N1 is N/2,
    powerOfTwo(N1).

/*
 * addValue(L,V,P)
 *   [] , L = []
 *   l1 U addValue(l2..ln, V, P+1) , powerOfTwo(P) = false
 *   l1 U V U addValue(l2..ln, V, P+1) , powerOfTwo(P) = true
 */

%addValue(L:list, V:integer, P:position, R:list)
%(i,i,i,o)
addValue([],_,_,[]).
addValue([H|T], V, P, [H|T1]):-
    not(powerOfTwo(P)),
    P1 is P+1,
    addValue(T, V, P1, T1).
addValue([H|T], V, P, [H,V|T1]):-
    powerOfTwo(P),
    P1 is P+1,
    addValue(T,V,P1,T1).

addValueMain(L,V,R):-
    addValue(L,V,1,R).



