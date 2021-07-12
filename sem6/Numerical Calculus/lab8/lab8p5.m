addpath(pwd)

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


f = @(x) 1/(4 + sin(20*x));

a=0;
b=pi;

simpsons10 = repeatedSimpson(f,a,b,10)
simpsons30 = repeatedSimpson(f,a,b,30)
