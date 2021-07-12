x = 0:0.01:1
f = exp(10*x.*(x-1)).*sin(12*pi*x)

figure(1)
plot(x,f)
title('Problem ||| 1 - f1')

x2 = 0:0.01:1
f2 = 3*exp(5*x2.^2-1).*cos(12*pi*x2)

figure(2)
plot(x2,f2)
title('Problem ||| 1 - f2')