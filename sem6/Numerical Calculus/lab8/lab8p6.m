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


f = @(x) 2/sqrt(pi)*e^(-x^2);

a=0;
b=0.5;

simpsons10 = repeatedSimpson(f,a,b,4)
simpsons30 = repeatedSimpson(f,a,b,10)


printf("Error with n = 10: %.10d\n", abs(simpsons10 - 0.520599876));
printf("Error with n = 30: %.10d\n", abs(simpsons30 - 0.520599876));
