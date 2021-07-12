addpath(pwd)

a = 1;
b = 1.5;
x = [a:0.01:b];

f = @(x) e.^(-x.^2);
result = (b-a) * f((a+b)/2);
printf("Integral evaluation: %.20d\n", result);

hold on;
fplot(f, [a, b]);
sh = fill([1, 1.5, 1.5, 1, 1], [0, 0, f(1.25), f(1.25), 0], 'b')
set(sh,'facealpha',.0)

n1 = 150;
n2 = 500;

function y = reapeated_rectangle(a,b,f,n)
  h = (b-a) / n;
  x1 = a + h/2;
  s = f(x1);
  i = [2:n];
  xi = x1 + (i-1) * h;
  s = s + sum(f(xi(1: end)));
  y = h * s;
end

printf("f for n = 150: %f\n", reapeated_rectangle(a, b, f, n1));
printf("f for n = 500: %f\n", reapeated_rectangle(a, b, f, n2));
