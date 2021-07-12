%sum(L,R)
%(i,o)
sum([],0).
sum([H|T],R):-sum(T,Rs), R is Rs + H.
