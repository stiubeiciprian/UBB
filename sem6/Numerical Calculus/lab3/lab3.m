addpath(pwd)

function A = computeA(nodes)
  A = ones(size(nodes));
  for i = 1:length(nodes)
    for j = 1:length(nodes)
      if i != j
        A(i) = A(i) / (nodes(i) - nodes(j));
      endif
    endfor
  endfor
endfunction

function L = lagrange(nodes, values, x)
  A = computeA(nodes);
  
  nominator = 0;
  denominator = 0;
  
  for i = 1:length(nodes)
    nominator = nominator + A(i) * values(i) ./(x - nodes(i));
    denominator = denominator + A(i) ./ (x - nodes(i));
  endfor  
  
  L = nominator/denominator;
endfunction



#P1
nodes = [1930 1940 1950 1960 1970 1980];
values = [123203 131669 150697 179323 203212 226505];

printf("Problem 1\n")
printf("1955 population: %e\n", lagrange(nodes, values, 1955))
printf("1995 population: %e\n", lagrange(nodes, values, 1995))

#P2
nodes = [100 121 144];
values = [10 11 12];

printf("---------------\nProblem 2\n")
printf("sqrt(115) = %d\n", lagrange(nodes, values, 115))

#P3
printf("---------------\nProblem 3\n")

title("Prolem 3")
f = @(x) (1 + cos(pi * x)) ./ (1 + x);

nodes = linspace(0, 10, 21);
values = f(nodes);
plot(nodes, values, 'r')
hold on
x = linspace(0, 10, 10);
plot(x, lagrange(nodes, values, x))
plot(x, f(x))



  
