addpath(pwd)

function Xnew = jacobi(A,b,no_iterations)
  Xold = zeros(size(b));
  Xnew = Xold;
  for k=1:no_iterations
    for i=1:length(b)
      Xnew(i) = 1/A(i,i) * (b(i)-A(i,1:i-1)*Xold(1:i-1)-...
      A(i,i+1:end)*Xold(i+1:end));
    endfor
    Xold = Xnew;
  endfor
endfunction


function X = gaussSeidel(A,b,no_iterations)
  X = zeros(size(b));
  for k=1:no_iterations
    for i=1:length(b)
      X(i) = 1/A(i,i) * (b(i)-A(i,1:i-1)*X(1:i-1)-...
      A(i,i+1:end)*X(i+1:end));
    endfor
  endfor
endfunction


function Xnew = sor(A,b,w,no_iterations)
  Xold = zeros(size(b));
  Xnew = Xold;
  for k=1:no_iterations
    for i=1:length(b)
      Xnew(i) = w*1/A(i,i) * (b(i)-A(i,1:i-1)*Xnew(1:i-1)-...
      A(i,i+1:end)*Xold(i+1:end))+(1-w)*Xold(i);
    endfor
    Xold = Xnew;
  endfor
endfunction


#for all matrix
n = 1000;
a = diag(-ones(n-1,1), -1) + diag(-ones(n-1,1), 1) + diag(3*ones(n,1), 0);
  
b = [2;ones(n-2,1);2];
s = jacobi(a,b,50);
gs = gaussSeidel(a,b,50);
sorr = sor(a,b,1.15,20);
[s,gs,sorr]

#[s2,nrIt,rho] = jacobi2(a,b);
#w = 2/(1+sqrt(1-rho^2));
#[gs2,nrIt2] = gaussSeidel2(a,b);
#[sorr2,nrIt3] = sor2(a,b,w);
#[nrIt,nrIt2,nrIt3]