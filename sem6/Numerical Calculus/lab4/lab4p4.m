addpath(pwd)

function A = aitken(nodes, values, x)
  m = length(nodes);
  A = zeros(m, m);
  A(:, 1) = transpose(values);
  
  for j = 2:m
    for i = j:m
      A(i, j) = 1 / (nodes(i) - nodes(j-1));
      t1 = A(j-1, j-1) * (nodes(i) - x);
      t2 = A(i, j-1) * (nodes(j-1) - x);
      A(i, j) *= t1 - t2;
    endfor
  endfor

endfunction

nodes = [64 61 100 121 144 169];
values = [8 9 10 11 12 13];

matrix = aitken(nodes, values, 115)

minError = inf;
matrixDiag = diag(matrix);

for i = 2:length(matrixDiag)
  error = abs(matrixDiag(i) - matrixDiag(i-1));
  if error < minError
    minError = error;
    bestApprox = matrixDiag(i);
  endif
  
  if minError < 0.001
    break;
  endif
endfor

printf("%.10d \n", bestApprox);
