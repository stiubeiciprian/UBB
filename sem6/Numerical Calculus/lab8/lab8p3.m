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

f = @(x) 60*r / (r^2-p^2) * (1 - (p/r)^2 * sin(x))^(1/2);
a=0;
b=2*pi;

trapezium = repeatedTrapezium(f,a,b,50)
trapezium = repeatedTrapezium(f,a,b,100)
