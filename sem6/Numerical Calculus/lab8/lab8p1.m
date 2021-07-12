addpath(pwd)

function A = repeatedTrapezium(f,a,b,n)
  A=0;
  h = (b-a)/n;
  ai = a;
  bi = ai+h;
  for i=1:n
    A +=  1/2 * (f(ai)+f(bi)) * h;
    ai = bi;
    bi = ai + h;
  endfor
endfunction

f = @(x) 2./(1+x.^2);
n=100;
a=0;
b=1;
integral = quad(f,a,b)

trapezium = repeatedTrapezium(f,a,b,n)


hold on;
fplot(f, [a, b]);
X = [0, 0];
Y = [0, f(0)];
Z = [1, f(1)];
C = [1, 0];
coor = [X ; Y; Z; C] ;  
sh = patch(coor(:,1), coor(:,2),'r');
set(sh,'facealpha',.3)


function A = repeatedSimpson(f,a,b,n)
  A=0;
  h = (b-a)/n;
  ai = a;
  bi = ai+h;
  for i=1:n
    A +=  h/6 * (f(ai) + 4*f((ai+bi)/2) + f(bi));
    ai = bi;
    bi = ai + h;
  endfor
endfunction

simpson = repeatedSimpson(f,a,b,n)
