addpath(pwd)

a = 1;
b = 3;
epsilon = 0.0001;
real_value = -1.4260247818;
f = @(x) 100./x.^2.*sin(10./x);
fplot(f, [a, b]);

function y = adquad(a, b, f, epsilon)
  y1 = simpson(a, b, f);
  y2 = simpson(a, (a+b)/2, f) + simpson((a+b)/2, b, f);
  
  if abs(y1 -y2) < 15 *epsilon
    y =y2;
    return;
  else
    y = adquad(a, (a+b)/2, f, epsilon/2) + adquad((a+b)/2, b, f, epsilon/2);
  end
end

function y = simpson(a, b, f)
  y = (b-a)/6 * (f(a) + f(b) + 4 * f(a + (b-a)/2));
end

function y = repeatedSimpson(a, b, f, n)
  h = (b-a)/n;
  xi = a:h:b;
  y = h/3 * (f(xi(1)) + 2*sum(f(xi(3:2:end-2))) + 4*sum(f(xi(2:2:end))) + f(xi(end)));
end


val_adquad = adquad(a, b, f, epsilon);
val_simpson1 = repeatedSimpson(a, b, f, 50);
val_simpson2 = repeatedSimpson(a, b, f, 100);

printf("Error adquad: %.20d\n", abs(val_adquad - real_value));
printf("Error with n = 50: %.20d\n", abs(val_simpson1 - real_value));
printf("Error with n = 100: %.20d\n", abs(val_simpson2 - real_value));
