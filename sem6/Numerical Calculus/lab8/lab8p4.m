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

p = 75
r = 110

f = @(x) x*log(x);
a=1;
b=2;

integral = quad(f,a,b)
trapezium = repeatedTrapezium(f,a,b,10)

