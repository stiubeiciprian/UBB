/*
 * 8. Generate all strings of n parenthesis correctly closed.
 * Eg: n=4 => (()) and () ()
 *
 */

%par(R)
%(o)
parentheses('(').
parentheses(')').


%verifySolution(L:list, R:integer)
%(i,o)
verifySolution([], 0).
verifySolution([H|T], C) :-
    H == '(',
    C1 is C + 1,
    verifySolution(T, C1).
verifySolution([H|T], C) :-
    H == ')',
    C > 0,
    C1 is C - 1,
    verifySolution(T, C1).


/*
 *  candidateSolution(N:integer, I:integer, S:list)
 *    S1..Sm , if N = I
 *    candidateSolution(N, I+1, parentheses() U S1..Sm)
 */

%candidateSolution(N:integer, I:integer , S:list , R:list)
%(i,i,i,o)
candidateSolution(N, N, S, S):-!.
candidateSolution(N, I, S, R):-
    parentheses(P),
    I1 is I + 1,
    candidateSolution(N, I1, [P|S], R).


/*
 *  generateSolution(N:integer)
 *    candidateSolution(N,0,[]), if verifySolution(candidateSolution(N,0,[])) = 0
 *
 */

%generateSolution(N:integer, R:string)
%(i,o)
generateSolution(N, Res):-
    candidateSolution(N, 0, [], R),
    verifySolution(R, 0),
    text_to_string(R,Res).


%generateAllSolutions(N:integer, R:list)
%(i,o)
generateAllSolutions(N, R):-
    findall(Res, generateSolution(N, Res), R).














